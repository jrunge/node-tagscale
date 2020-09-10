{ "targets": [{
  "target_name": "NativeExtension",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "xcode_settings": { "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.7",
      },
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },
      },
  "sources": [ "NativeExtension.cc", "functions.cc" ],
  "arflags": [ "cr" ],
  "cflags_cc": [ "-O3", "-static", "-fPIC","-rdynamic","-Wl,-whole-archive" ],
  "cxxflags_cc": [ "-static", "-fPIC","-rdynamic","-Wl,-whole-archive" ],
  "cflags!": [ "-fno-exceptions" ],
  "cflags_cc!": [ "-fno-exceptions" ],
  "libraries": [
    "-L ../upscaledb/3rdparty/murmurhash3",
    "-L ../upscaledb/3rdparty/simdcomp",
    "-L ../upscaledb/3rdparty/liblzf",
    "../upscaledb/dest/lib/libupscaledb.a" ],
  'conditions': [
      ['OS=="mac"', {
        'ldflags': [
          "-lboost_thread-mt", "-lpthread", "-lboost_filesystem", "-lz", "-ldl",
        ],
        "libraries": [
          "-L <!(dirname $(find /usr/lib -name libz.dylib | head -n1))",
        ],
      }],
      ['OS=="linux"', {
        'ldflags': [
          "-lboost_thread", "-lpthread", "-lboost_filesystem", "-lz", "-ldl",
        ],
        "libraries": [
          "-L <!(dirname $(find /usr/lib -name libz.a | head -n1))",
        ],
      }],
  ],
  "include_dirs" : [ 'upscaledb/include', "<!@(node -p \"require('node-addon-api').include\")" ],
  "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ]
}]}
