cc_library(
	name = "liblambda",
	srcs = glob(["src/**/*.cc"]),
	hdrs = glob(["include/lambda/**/*.hh"]),
	copts = ["-Iinclude/lambda", "-isystem external/geneous/include"],
	deps = [
		"@geneous//:main"
	]
)