#pragma once
#ifndef _AUTYP_H
# define _AUTYP_H

#define OPER(X, ...) virtual inline thistyp operator##X##(thistyp) = 0; __VA_OPT__(OPER(__VA_ARGV__))

==,!=,>,<,>=,=<,&,|,^,&&,||
namespace AUTYP {
	struct coretyp {
		private using thistyp = this auto;
		OPER(+, -, *, /, ^, ==, !=, >, <, >=, =<, &, |, &&, ||)
	}
}

#undef OPER

#endif
