/* ----------------------------------------------------------------
    * NYX Protocol Source Code
    * DO NOT DISTRIBUTE TO PARTICIPANTS! ADMIN ONLY!
    * * ---------------------------------------------------------------- */

#include <stdio.h>
#include <string.h>

#define LEN 8

/* ----------------------------------------------------------------
 * rol() -- 1-bit left circular rotation
 * ---------------------------------------------------------------- */
static unsigned char rol(unsigned char val) {
    return (unsigned char)((val << 1) | (val >> 7));
}

/* ----------------------------------------------------------------
 * xor_decode() -- decode a buffer in place with key 0x42
 * ---------------------------------------------------------------- */
static void xor_decode(unsigned char *buf, int len) {
    for (int i = 0; i < len; i++) {
        buf[i] ^= 0x42;
    }
}

/* ----------------------------------------------------------------
 * print_decoded() -- decode, print, then zero the buffer
 * ---------------------------------------------------------------- */
static void print_decoded(unsigned char *buf, int len) {
    xor_decode(buf, len);
    for (int i = 0; i < len; i++) {
        putchar((int)buf[i]);
    }
    memset(buf, 0, (size_t)len);
}

/* ----------------------------------------------------------------
 * build_target() -- constructs the expected comparison buffers.
 *
 * A seed evolves through a linear congruential step each round.
 * At each position the seed is XORed with a position-specific
 * mask to produce each target byte.
 * Two valid keys are accepted; their masks are stored here.
 * ---------------------------------------------------------------- */
static void build_target(unsigned char *t1, unsigned char *t2) {
    static const unsigned char masks1[LEN] = {
        0x8a, 0x1e, 0x61, 0xe8, 0x67, 0x96, 0x97, 0xf4
    };
    static const unsigned char masks2[LEN] = {
        0xba, 0x3a, 0x37, 0x58, 0x0f, 0x44, 0x23, 0xc6
    };

    unsigned char seed = 0x5A;
    for (int i = 0; i < LEN; i++) {
        seed  = (unsigned char)((seed * 3 + 7) & 0xFF);
        t1[i] = seed ^ masks1[i];
        t2[i] = seed ^ masks2[i];
    }
}

/* ----------------------------------------------------------------
 * validate() -- transforms input and compares against both targets.
 * Returns:  1 = correct key
 *           0 = wrong key
 *          -1 = wrong length
 * ---------------------------------------------------------------- */
static int validate(char *input) {
    if ((int)strlen(input) != LEN) {
        return -1;
    }

    unsigned char buf[LEN];
    unsigned char t1[LEN];
    unsigned char t2[LEN];

    for (int i = 0; i < LEN; i++) {
        buf[i] = (unsigned char)input[i];
    }

    /* Stateful transformation:
     *   1. Rotate byte left by 1
     *   2. XOR with running state
     *   3. State advances using the transformed byte
     * Each byte's result depends on all previous bytes. */
    unsigned char state = 0x33;
    for (int i = 0; i < LEN; i++) {
        buf[i]  = rol(buf[i]);
        buf[i] ^= state;
        state   = (unsigned char)((state + buf[i]) & 0xFF);
    }

    build_target(t1, t2);

    int match = 0;
    int m1 = 1, m2 = 1;
    for (int i = 0; i < LEN; i++) {
        if (buf[i] != t1[i]) m1 = 0;
        if (buf[i] != t2[i]) m2 = 0;
    }
    match = (m1 || m2);

    memset(buf, 0, LEN);
    memset(t1,  0, LEN);
    memset(t2,  0, LEN);

    return match;
}

int main(void) {
    /* All sensitive strings are XOR-encoded with key 0x42.
     * Nothing meaningful appears in `strings` output.          */

    /* 'Nyx Protocol Initialized.' */
    unsigned char msg_banner[] = {
        0x0c,0x3b,0x3a,0x62,0x12,0x30,0x2d,0x36,0x2d,0x21,
        0x2d,0x2e,0x62,0x0b,0x2c,0x2b,0x36,0x2b,0x23,0x2e,
        0x2b,0x38,0x27,0x26,0x6c
    };

    /* '\nAccess Granted.\nFlag: ' */
    unsigned char msg_granted[] = {
        0x48,0x03,0x21,0x21,0x27,0x31,0x31,0x62,0x05,0x30,
        0x23,0x2c,0x36,0x27,0x26,0x6c,0x48,0x04,0x2e,0x23,
        0x25,0x78,0x62
    };

    /* 'NYX{d4rkn355_r3qu1r35_d3p7h}' */
    unsigned char flag_enc[] = {
        0x0c,0x1b,0x1a,0x39,0x26,0x76,0x30,0x29,0x2c,0x71,
        0x77,0x77,0x1d,0x30,0x71,0x33,0x37,0x73,0x30,0x71,
        0x77,0x1d,0x26,0x71,0x32,0x75,0x2a,0x3f
    };

    char input[100];

    print_decoded(msg_banner, (int)sizeof(msg_banner));
    putchar('\n');

    while (1) {
        /* Prompt rebuilt each iteration — decode-in-place
         * would zero it, so a fresh copy is used each time. */

        /* 'Enter 8-character access key: ' */
        unsigned char prompt[] = {
            0x07,0x2c,0x36,0x27,0x30,0x62,0x7a,0x6f,0x21,0x2a,
            0x23,0x30,0x23,0x21,0x36,0x27,0x30,0x62,0x23,0x21,
            0x21,0x27,0x31,0x31,0x62,0x29,0x27,0x3b,0x78,0x62
        };
        print_decoded(prompt, (int)sizeof(prompt));
        fflush(stdout);

        if (scanf("%99s", input) != 1) {
            putchar('\n');
            break;
        }

        int result = validate(input);
        memset(input, 0, sizeof(input));

        if (result == -1) {
            /* 'Invalid key length.' */
            unsigned char bl[] = {
                0x0b,0x2c,0x34,0x23,0x2e,0x2b,0x26,0x62,0x29,
                0x27,0x3b,0x62,0x2e,0x27,0x2c,0x25,0x36,0x2a,0x6c
            };
            print_decoded(bl, (int)sizeof(bl));
            putchar('\n');
            continue;
        }

        if (result == 1) {
            print_decoded(msg_granted, (int)sizeof(msg_granted));
            print_decoded(flag_enc,    (int)sizeof(flag_enc));
            putchar('\n');
            break;
        }

        /* 'Access Denied.' */
        unsigned char dn[] = {
            0x03,0x21,0x21,0x27,0x31,0x31,0x62,0x06,0x27,
            0x2c,0x2b,0x27,0x26,0x6c
        };
        print_decoded(dn, (int)sizeof(dn));
        putchar('\n');
    }

    return 0;
}