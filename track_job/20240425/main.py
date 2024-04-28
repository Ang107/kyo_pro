import sys
import pandas as pd
from typing import List, Dict
from datetime import datetime
import re

# 定数の定義
REQUIRED_ARGV_LEN = 3
REQUIRED_AGGREGATE_MODES = {"highscore", "average"}
REQUIRED_ENTRY_COLUMNS = ["create_timestamp", "player_id", "handle_name"]
REQUIRED_SCORE_COLUMNS = ["create_timestamp", "player_id", "score"]
HEADER = ["rank", "player_id", "handle_name", "score"]


def read_csv_with_error_handling(file_path: str) -> pd.DataFrame:
    """
    指定されたファイルパスからCSVファイルを読み込み、文字列型としてDataFrameを返します。
    ファイルが見つからない、空、または解析できない場合は、適切な例外を発生させます。
    """
    try:
        return pd.read_csv(file_path, dtype=str)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"エラー: 指定されたファイル '{file_path}' が存在しません。"
        )
    except pd.errors.EmptyDataError:
        raise ValueError(f"エラー: 指定されたファイル '{file_path}'が空です。")
    except pd.errors.ParserError:
        raise ValueError(
            f"エラー: 指定されたファイル '{file_path}'の解析に失敗しました。"
        )
    except Exception as e:
        raise Exception(f"予期せぬエラーが発生しました: {str(e)}")


def validate_data_format(
    df: pd.DataFrame, required_columns: List[str], file_path: str
) -> None:
    """
    指定されたDataFrameのカラムを確認し、必要なカラムが含まれていること、
    欠損している値が無いこと、および各カラムのデータが指定されたフォーマットに合致していることを検証します。
    """
    if df.isnull().values.sum() != 0:
        raise ValueError(f"エラー: '{file_path}' の中に欠損している値があります。")

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]
    if missing_columns:
        raise ValueError(
            f"エラー: '{file_path}' 内に必要なカラム '{', '.join(missing_columns)}' が存在しません。"
        )

    for column in required_columns:
        invalid_data = [
            val for _, val in df[column].items() if not check_format(column, val)
        ]
        if invalid_data:
            raise ValueError(
                f"エラー: '{file_path}' の '{column}' 内に不適切なフォーマットのデータが見つかりました。 不適切なデータ: '{', '.join(invalid_data)}'"
            )


def process_entry_and_score_logs(
    entry_log_path: str,
    score_log_path: str,
) -> None:
    """
    指定されたエントリーログとスコアログのCSVファイルを読み込み、
    それぞれのフォーマットを検証後、2つのDataFrameを返します。
    """
    entry_log = read_csv_with_error_handling(entry_log_path)
    score_log = read_csv_with_error_handling(score_log_path)
    validate_data_format(entry_log, REQUIRED_ENTRY_COLUMNS, entry_log_path)
    validate_data_format(score_log, REQUIRED_SCORE_COLUMNS, score_log_path)
    return entry_log, score_log


def check_format(column_name: str, val: str) -> bool:
    """
    特定のカラムに対して値が指定されたフォーマット要件を満たしているかをチェックします。
    """
    match column_name:
        case "create_timestamp":
            try:
                datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
                return True
            except ValueError:
                return False
        case "player_id":
            return bool(re.match(r"^[a-zA-Z0-9_]{1,20}$", val))
        case "handle_name":
            return bool(re.match(r"^[a-zA-Z0-9_]{1,20}$", val))
        case "score":
            return bool(re.match(r"^\d+$", val)) and int(val) >= 0


class Player:
    """
    プレイヤー情報を管理するクラスです。プレイヤーID、ハンドル名、最初のエントリー時刻、
    スコアリスト、およびフォーカススコアを属性として持ちます。
    """

    def __init__(self, player_id: str, handle_name: str, first_entry_time: str) -> None:
        self.__player_id = player_id
        self.__handle_name = handle_name
        self.__first_entry_time = first_entry_time
        self.__score_list = []
        self.__focus_score = -1

    def update_handle_name(self, new_handle_name) -> None:
        self.__handle_name = new_handle_name

    @property
    def player_id(self) -> str:
        return self.__player_id

    @property
    def handle_name(self) -> str:
        return self.__handle_name

    @property
    def first_entry_time(self) -> str:
        return self.__first_entry_time

    @property
    def focus_score(self) -> int:
        return self.__focus_score

    def add_score(self, score: int) -> None:
        self.__score_list.append(score)

    def set_focus_score(self, aggregate_mode: str) -> None:
        if aggregate_mode == "highscore":
            if self.__score_list:
                self.__focus_score = max(self.__score_list)
        elif aggregate_mode == "average":
            if len(self.__score_list) >= 10:
                self.__focus_score = round(
                    sum(self.__score_list) / len(self.__score_list)
                )


def get_summary_data(
    entry_log: pd.DataFrame, score_log: pd.DataFrame
) -> Dict[str, Player]:
    """
    エントリーログとスコアログからプレイヤーごとのサマリーデータを集計します。
    """
    summary_data = {}
    for timestamp, player_id, handle_name in entry_log.itertuples(index=False):
        if player_id not in summary_data:
            summary_data[player_id] = Player(player_id, handle_name, timestamp)
        else:
            summary_data[player_id].update_handle_name(handle_name)

    for timestamp, player_id, score in score_log.itertuples(index=False):
        if (
            player_id in summary_data
            and timestamp >= summary_data[player_id].first_entry_time
        ):
            summary_data[player_id].add_score(int(score))

    return summary_data


def get_sorted_data(
    summary_data: Dict[str, Player], aggregate_mode: str
) -> List[Player]:
    """
    集計モードに基づき、プレイヤーのデータをソートします。
    """
    for player in summary_data.values():
        player.set_focus_score(aggregate_mode)
    sorted_data = sorted(
        summary_data.values(),
        key=lambda x: (-x.focus_score, x.first_entry_time, x.player_id),
    )
    return sorted_data


def get_filtered_data(sorted_data: List[Player]) -> List[Player]:
    """
    フォーカススコアが0以上のプレイヤーのデータのみをフィルタリングします。
    """
    return [player for player in sorted_data if player.focus_score >= 0]


def get_aggregate_data(
    entry_log: pd.DataFrame, score_log: pd.DataFrame, aggregate_mode: str
) -> pd.DataFrame:
    """
    エントリーログとスコアログから集計データを生成し、ソートおよびフィルタリングを行った結果を返します。
    """
    summary_data = get_summary_data(entry_log, score_log)
    sorted_data = get_sorted_data(summary_data, aggregate_mode)
    filtered_data = get_filtered_data(sorted_data)
    return filtered_data


def check_argv(argv: List[str]) -> None:
    """
    コマンドライン引数を検証します。引数の数と集計モードの適切さをチェックします。
    """
    if len(argv) != REQUIRED_ARGV_LEN:
        raise ValueError(
            f"エラー: コマンドライン引数の数が不適切です。必要な引数の数: {REQUIRED_ARGV_LEN}, 与えられた引数の数: {len(argv)}"
        )
    if argv[0] not in REQUIRED_AGGREGATE_MODES:
        raise ValueError(
            f"エラー: 第一引数の集計モード '{argv[0]}' が不適切です。有効なモード: {', '.join(REQUIRED_AGGREGATE_MODES)}"
        )


def output(data: List[Player]) -> None:
    """
    集計結果を標準出力に表示します。ヘッダーとデータをCSV形式で出力します。
    """
    print(",".join(HEADER))
    rank = 0
    score = float("inf")
    for index, player in enumerate(data):
        if score > player.focus_score:
            score = player.focus_score
            rank = index + 1
        if rank <= 10:
            print(
                f"{rank},{player.player_id},{player.handle_name},{player.focus_score}"
            )
        else:
            break


def main(argv: List[str]) -> None:
    """
    メイン関数。コマンドライン引数を受け取り、適切な処理を行い、結果を出力します。
    """
    try:
        check_argv(argv)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

    aggregate_mode = argv[0]
    entry_log_path = argv[1]
    score_log_path = argv[2]

    try:
        entry_log, score_log = process_entry_and_score_logs(
            entry_log_path,
            score_log_path,
        )
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

    aggregate_data = get_aggregate_data(entry_log, score_log, aggregate_mode)
    output(aggregate_data)
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
