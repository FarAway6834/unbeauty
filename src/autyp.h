#pragma once
#ifndef _AUTYP_H
# define _AUTYP_H

#define OPER(X, ...) virtual inline thistyp operator##X##(thistyp) = 0; __VA_OPT__(OPER(__VA_ARGV__))
#define THIST private using thistyp = this auto;

namespace AUTYP {
	typedef void* autolike;
	struct coretyp {
		THIST
		OPER(+, -, *, /, ^, ==, !=, >, <, >=, =<, &, |, &&, ||)
		template <autolike B>
		struct __optlib_handle__;
	};

	template <typename T, T X>
	struct holder {
		using typ = T;
		T V = X;
	}

	template <typename T>
	constexpr inline T tempv(void) {
		constexpr static T v;
		return v;
	};

	template <typename RET, typename... ARGV, DUMMY = tempv<RET>()>
	struct see_plan_md {
		struct subclstypes {
			THIST
			final inline RET operator[](ARGV... argv...) {
				return (this.cache(true, RET DUMMY, argv...) == 1)?this.cache(false, this(argv...), argv...):this(false, DUMMY, argv ...);
			};
			final inline RET operator()(ARGV... argv...) {
				return this::__TMP__<argv...>
			};
			protected virtual inline RET v cache(bool check, RET v, ARGV... argv...) = 0;
		};
	};
}

#undef OPER

#endif
