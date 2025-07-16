#pragma once
#ifndef _AUTYP_H
# define _AUTYP_H

#define OPER(X, ...) virtual inline thistyp operator##X##(thistyp) = 0; __VA_OPT__(OPER(__VA_ARGV__))

namespace AUTYP {
	typedef void* autolike;
	struct coretyp {
		private using thistyp = this auto;
		OPER(+, -, *, /, ^, ==, !=, >, <, >=, =<, &, |, &&, ||)
		template <autolike B>
		struct __optlib_handle__;
	};

	template <typename T, T X>
	struct holder {
		using typ = T;
		T V = X;
	}

	template <typename... ARGV, typename RET, RET DUMMY>
	struct subclstypes {
		final inline RET operator[](ARGV... argv...) {
			return (this.cache(true, RET DUMMY, argv...) == 1)?this.cache(false, this(argv...), argv...):this(false, DUMMY, argv ...);
		};
		virtual inline RET operator()(ARGV... argv...) = 0;
		protected virtual inline RET v cache(bool check, RET v, ARGV... argv...) = 0;
	};
}

#undef OPER

#endif
