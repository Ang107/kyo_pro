// #pragma GCC optimize
// "-O3,omit-frame-pointer,inline,unroll-all-loops,fast-math" #pragma GCC target
// "tune=native"
#include <bits/stdc++.h>
// INCLUDE <experimental/simd>
// INCLUDE <atcoder/all>
#include <ext/pb_ds/assoc_container.hpp>
// #include <immintrin.h>
// #include <sys/time.h>
// #include <x86intrin.h>

using namespace std;
// Macros
#define el '\n'
#define all(v) (v).begin(), (v).end()
using i8 = int8_t;
using u8 = uint8_t;
using i16 = int16_t;
using u16 = uint16_t;
using i32 = int32_t;
using u32 = uint32_t;
using i64 = int64_t;
using u64 = uint64_t;
using f32 = float;
using f64 = double;
#define rep(i, n) for (i64 i = 0; i < (i64)(n); i++)
template <class T> using min_queue = priority_queue<T, vector<T>, greater<T>>;
template <class T> using max_queue = priority_queue<T>;
struct uint64_hash {
    static inline uint64_t rotr(uint64_t x, unsigned k) {
        return (x >> k) | (x << (8U * sizeof(uint64_t) - k));
    }
    static inline uint64_t hash_int(uint64_t x) noexcept {
        auto h1 = x * (uint64_t)(0xA24BAED4963EE407);
        auto h2 = rotr(x, 32U) * (uint64_t)(0x9FB21C651E98DF25);
        auto h = rotr(h1 + h2, 32U);
        return h;
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM =
            std::chrono::steady_clock::now().time_since_epoch().count();
        return hash_int(x + FIXED_RANDOM);
    }
};
template <typename K, typename V, typename Hash = uint64_hash>
using hash_map = __gnu_pbds::gp_hash_table<K, V, Hash>;
template <typename K, typename Hash = uint64_hash>
using hash_set = hash_map<K, __gnu_pbds::null_type, Hash>;

// Constant
constexpr bool DEBUG = true;
const double pi = 3.141592653589793238;
const i32 inf32 = 1073741823;
const i64 inf64 = 1LL << 60;
const string ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string abc = "abcdefghijklmnopqrstuvwxyz";
const int MOD = 998244353;
const array<int, 8> dx = {0, 0, -1, 1, -1, -1, 1, 1};
const array<int, 8> dy = {-1, 1, 0, 0, -1, 1, -1, 1};

// Printing
template <class T> void print_collection(ostream &out, T const &x);
template <class T, size_t... I>
void print_tuple(ostream &out, T const &a, index_sequence<I...>);
namespace std {
template <class... A> ostream &operator<<(ostream &out, tuple<A...> const &x) {
    print_tuple(out, x, index_sequence_for<A...>{});
    return out;
}
template <class... A> ostream &operator<<(ostream &out, pair<A...> const &x) {
    print_tuple(out, x, index_sequence_for<A...>{});
    return out;
}
template <class A, size_t N>
ostream &operator<<(ostream &out, array<A, N> const &x) {
    print_collection(out, x);
    return out;
}
template <class A> ostream &operator<<(ostream &out, vector<A> const &x) {
    print_collection(out, x);
    return out;
}
template <class A> ostream &operator<<(ostream &out, deque<A> const &x) {
    print_collection(out, x);
    return out;
}
template <class A> ostream &operator<<(ostream &out, multiset<A> const &x) {
    print_collection(out, x);
    return out;
}
template <class A, class B>
ostream &operator<<(ostream &out, multimap<A, B> const &x) {
    print_collection(out, x);
    return out;
}
template <class A> ostream &operator<<(ostream &out, set<A> const &x) {
    print_collection(out, x);
    return out;
}
template <class A, class B>
ostream &operator<<(ostream &out, map<A, B> const &x) {
    print_collection(out, x);
    return out;
}
template <class A, class B>
ostream &operator<<(ostream &out, unordered_set<A> const &x) {
    print_collection(out, x);
    return out;
}
} // namespace std
template <class T, size_t... I>
void print_tuple(ostream &out, T const &a, index_sequence<I...>) {
    using swallow = int[];
    out << '(';
    (void)swallow{0, (void(out << (I == 0 ? "" : ", ") << get<I>(a)), 0)...};
    out << ')';
}
template <class T> void print_collection(ostream &out, T const &x) {
    int f = 0;
    out << '[';
    for (auto const &i : x) {
        out << (f++ ? "," : "");
        out << i;
    }
    out << "]";
}
// Random
struct RNG {
    uint64_t s[2];
    RNG(u64 seed) { reset(seed); }
    RNG() { reset(time(0)); }
    using result_type = u32;
    constexpr u32 min() { return numeric_limits<u32>::min(); }
    constexpr u32 max() { return numeric_limits<u32>::max(); }
    u32 operator()() { return randomInt32(); }
    static __attribute__((always_inline)) inline uint64_t rotl(const uint64_t x,
                                                               int k) {
        return (x << k) | (x >> (64 - k));
    }
    inline void reset(u64 seed) {
        struct splitmix64_state {
            u64 s;
            u64 splitmix64() {
                u64 result = (s += 0x9E3779B97f4A7C15);
                result = (result ^ (result >> 30)) * 0xBF58476D1CE4E5B9;
                result = (result ^ (result >> 27)) * 0x94D049BB133111EB;
                return result ^ (result >> 31);
            }
        };
        splitmix64_state sm{seed};
        s[0] = sm.splitmix64();
        s[1] = sm.splitmix64();
    }
    uint64_t next() {
        const uint64_t s0 = s[0];
        uint64_t s1 = s[1];
        const uint64_t result = rotl(s0 * 5, 7) * 9;
        s1 ^= s0;
        s[0] = rotl(s0, 24) ^ s1 ^ (s1 << 16); // a, b
        s[1] = rotl(s1, 37);                   // c
        return result;
    }
    inline u32 randomInt32() { return next(); }
    inline u64 randomInt64() { return next(); }
    inline u32 random32(u32 r) { return (((u64)randomInt32()) * r) >> 32; }
    inline u64 random64(u64 r) { return randomInt64() % r; }
    inline u32 randomRange32(u32 l, u32 r) { return l + random32(r - l + 1); }
    inline u64 randomRange64(u64 l, u64 r) { return l + random64(r - l + 1); }
    inline double randomDouble() {
        return (double)randomInt32() / 4294967296.0;
    }
    inline float randomFloat() { return (float)randomInt32() / 4294967296.0; }
    inline double randomRangeDouble(double l, double r) {
        return l + randomDouble() * (r - l);
    }
    template <class T> void shuffle(vector<T> &v) {
        i32 sz = v.size();
        for (i32 i = sz; i > 1; i--) {
            i32 p = random32(i);
            swap(v[i - 1], v[p]);
        }
    }
    template <class T> void shuffle(T *fr, T *to) {
        i32 sz = distance(fr, to);
        for (int i = sz; i > 1; i--) {
            int p = random32(i);
            swap(fr[i - 1], fr[p]);
        }
    }
    template <class T> inline int sample_index(vector<T> const &v) {
        return random32(v.size());
    }
    template <class T> inline T sample(vector<T> const &v) {
        return v[sample_index(v)];
    }
} rng;
// Timer
struct timer {
    chrono::high_resolution_clock::time_point t_begin;
    timer() { t_begin = chrono::high_resolution_clock::now(); }
    void reset() { t_begin = chrono::high_resolution_clock::now(); }
    float elapsed() const {
        return chrono::duration<float>(chrono::high_resolution_clock::now() -
                                       t_begin)
            .count();
    }
};
// Util
template <class T> T &smin(T &x, T const &y) {
    x = min(x, y);
    return x;
}
template <class T> T &smax(T &x, T const &y) {
    x = max(x, y);
    return x;
}
template <typename T> int sgn(T val) {
    if (val < 0)
        return -1;
    if (val > 0)
        return 1;
    return 0;
}
static inline string int_to_string(int val, int digits = 0) {
    string s = to_string(val);
    reverse(begin(s), end(s));
    while ((int)s.size() < digits)
        s.push_back('0');
    reverse(begin(s), end(s));
    return s;
}
// Debug
static inline void debug() { cerr << "\n"; }
template <class T, class... V> void debug(T const &t, V const &...v) {
    if (DEBUG) {
        cerr << t;
        if (sizeof...(v)) {
            cerr << ", ";
        }
        debug(v...);
    }
}
// Bits
__attribute__((always_inline)) inline u64 bit(u64 x) { return 1ull << x; }
__attribute__((always_inline)) inline void setbit(u64 &a, u32 b,
                                                  u64 value = 1) {
    a = (a & ~bit(b)) | (value << b);
}
__attribute__((always_inline)) inline u64 getbit(u64 a, u32 b) {
    return (a >> b) & 1;
}
__attribute__((always_inline)) inline u64 lsb(u64 a) {
    return __builtin_ctzll(a);
}
__attribute__((always_inline)) inline int msb(uint64_t bb) {
    return __builtin_clzll(bb) ^ 63;
}
struct Init {
    Init() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
} init;

struct Input {
    // todo
    void input() {}
};
class Solver {
    // to do
    Solver() {}
    void solve() {}
    void print() {}
};
int main() {
    // todo
}