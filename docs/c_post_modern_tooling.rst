Post modern C tooling
=====================

| Contemporary
  `C <https://en.wikipedia.org/wiki/C_(programming_language)>`__ tooling
  for making higher quality C, faster or more safely.
| In 2001 or so people started using the phrase "Modern C++". So now
  that it's 2019, I guess we're in the post modern era? Anyway, this
  isn't a post about C++ code, but some of this information applies
  there too.

==================================
|image0|
No logo, but it's used everywhere.
==================================

|

Welcome to the post modern era.
-------------------------------

| Some of the C++ people have pulled off one of the cleverest and
  sneakiest tricks ever. They required 'modern'
  `C99 <https://en.wikipedia.org/wiki/C99>`__ and
  `C11 <https://en.wikipedia.org/wiki/C11_(C_standard_revision)>`__
  features in 'recent' C++ standards. Microsoft has famously still clung
  onto some 80s version of C with their compiler for the longest time.
  So it's been a decade of hacks for people writing portable code in C.
  For a while I thought we'd be stuck in the 80s with C89 forever.
  However, now that some C99 and C11 features are more widely available
  in the Microsoft compiler, we can use these features in highly
  portable code (but forget about C17/C18 ISO/IEC 9899:2018/C2X
  stuff!!). Check out the `"New" Features in
  C <https://www.youtube.com/watch?v=ieERUEhs910>`__ talk, and the
  `Modern C <https://modernc.gforge.inria.fr/>`__ book for more details.
| So, we have some pretty new language features in C with C11.  But what
  about tooling?

Tools and protection for our feet.
----------------------------------

| C, whilst a work horse being used in everything from toasters, trains,
  phones, web browsers, ... (everything basically) - is also an
  excellent tool for shooting yourself in the foot.

   .. rubric:: Noun
      :name: noun

   | **footgun** (*plural*
     `footguns <https://en.wiktionary.org/wiki/footguns#English>`__)

   #. (\ `informal <https://en.wiktionary.org/wiki/Appendix:Glossary#informal>`__\ \ ,\ `humorous <https://en.wiktionary.org/wiki/humorous>`__\ \ ,\ `derogatory <https://en.wiktionary.org/wiki/derogatory>`__\ )
      Any `feature <https://en.wiktionary.org/wiki/feature>`__ whose
      addition to a product results in the user `shooting themselves in
      the
      foot <https://en.wiktionary.org/wiki/shoot_oneself_in_the_foot>`__.
      C.

|
| Tools like linters, test coverage checkers, static analyzers, memory
  checkers, documentation generators, thread checkers, continuous
  integration, nice error messages, ... and such help protect our feet.
| How do we do continuous delivery with a language that lets us do the
  most low level footgunie things ever? On a dozen CPU architectures, 32
  bit, 64bit, little endian, big endian, 64 bit with 32bit pointers
  (wat?!?), with multiple compilers, on a dozen different OS, with
  dozens of different versions of your dependencies?
| Surely there won't be enough time to do releases, and have time left
  to eat my vegan shaved ice desert after lunch?

Debuggers
---------

   Give me 15 minutes, and I'll change your mind about GDB. --
   https://www.youtube.com/watch?v=PorfLSr3DDI

| Firstly, did you know gdb had a curses based 'GUI' which works in a
  terminal? It's a quite a bit easier to use than the command line text
  interface. It's called TUI. It's built in, and uses emacs key
  bindings.
| But what if you are used to VIM key bindings?
  `cgdb <https://cgdb.github.io/>`__ to the rescue.

=======================
|image1|
https://cgdb.github.io/
=======================

|
| VIM has integrated gdb debugging with
  `TermDebug <https://www.dannyadam.com/blog/2019/05/debugging-in-vim/>`__
  since version 8.1.
| Also, there's a fairly easy to use web based front end for GDB called
  `gdbgui <https://www.gdbgui.com/>`__
|  (https://www.gdbgui.com/). For those who don't use an IDE with
  debugging support built in (such as Visual studio by Microsoft or
  XCode by Apple).

Reverse debugger
~~~~~~~~~~~~~~~~

| Normally a program runs forwards. But what about when you are
  debugging and you want to run the program backwards?

   Set breakpoints and data watchpoints and quickly reverse-execute to
   where they were hit.

|
| How do you tame non determinism to allow a program to run the same way
  it did when it crashed? In C and with threads some times it's really
  hard to reproduce problems.
| rr helps with this. It's actual magic.
| https://rr-project.org/



LLDB - the LLVM debugger.
~~~~~~~~~~~~~~~~~~~~~~~~~

| Apart from the ever improving
  `gdb <https://www.gnu.org/software/gdb/>`__, there is a new debugger
  from the LLVM people - `lldb <https://lldb.llvm.org/>`__ (
  https://lldb.llvm.org/ ).

IDE debugging
~~~~~~~~~~~~~

| Visual Studio by Microsoft, and XCode by Apple are the two heavy
  weights here.
| The free Visual Studio Code also supports debugging with GDB.
  https://code.visualstudio.com/docs/languages/cpp
| Sublime is another popular editor, and there is good GDB integration
  for it too in the `SublimeGDB
  package <https://packagecontrol.io/packages/SublimeGDB>`__
  (https://packagecontrol.io/packages/SublimeGDB).

Windows debugging
~~~~~~~~~~~~~~~~~

| Suppose you want to do post mortem debugging? With
  `procdump <https://docs.microsoft.com/en-us/sysinternals/downloads/procdump>`__
  and
  `WinDbg <https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools>`__
  you can. "`How to take a
  procdump <https://blogs.msdn.microsoft.com/webdav_101/2018/03/20/how-to-take-a-procdump/>`__"
  (https://blogs.msdn.microsoft.com/webdav_101/2018/03/20/how-to-take-a-procdump/)
  is a nice tutorial on how to use procdump.
|     Launch a process and then monitor it for exceptions:
|     C:\> procdump -e 1 -f "" -x c:\dumps consume.exe
| This makes some process dumps when it crashes, which you can then open
  with
  `WinDbg <https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugging-using-windbg-preview>`__\ (https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugging-using-windbg-preview).

Portable building, and package management
-----------------------------------------

| C doesn't have a package manager... or does it?
| Ever since Debian dpkg, Redhat rpm, and Perl started doing package
  management in the early 90s people world wide have been able to share
  pieces of software more easily. Following those systems, many other
  systems like Ruby gems, JavaScript npm, and Pythons cheese shop came
  into being. Allowing many to share code easily.
| But what about C? How can we define dependencies on different
  'packages' or libraries and have them compile on different platforms?
| How do we build with Microsofts compiler, with gcc, with clang, or
  Intels C compiler? How do we build on Mac, on Windows, on Ubuntu, on
  Arch linux? Sometimes we want to use an Integrated Development
  Environment (IDE) because they provide lots of nice tools. But maybe
  also three IDEs (XCode, Microsoft Visual C, CLion, ...) depending on
  platform. But we don't want to have to keep several IDE project files
  up to date. But we also want to integrate nicely with different OS
  packagers like Debian, FreeBSD. We want people to be able to use
  apt-get install for their dependencies if they want. We also want to
  cross compile code on our beefy workstations to work on
  microcontrollers or slower low memory systems (like earlier
  RaspberryPi systems).

The Meson Build System.
~~~~~~~~~~~~~~~~~~~~~~~

| If CMake is modern, then `The Meson Build
  System <https://mesonbuild.com/index.html>`__
  (https://mesonbuild.com/index.html) is post modern.

   "Meson is an open source build system meant to be both extremely
   fast, and, even more importantly, as **user friendly as possible.**

..

   The main design point of Meson is that every moment a developer
   spends writing or debugging build definitions is a second wasted. So
   is every second spent waiting for the build system to actually start
   compiling code."

| It's first major user was GStreamer, a multi platform multimedia
  toolkit which is highly portable. Now it is especially popular in the
  FreeDesktop world with projects like gstreamer, GTK, and systemd
  amongst many others using it.
| The documentation is excellent, and it's very fast compared to
  autotools or cmake. https://www.youtube.com/watch?v=SCZLnopmYBM
  https://www.youtube.com/watch?v=gHdTzdXkhRY
| Example meson.build for example
  project\ `polysnake <https://github.com/jpakkane/polysnake>`__\ (https://github.com/jpakkane/polysnake):
  "A Python extension module that uses C, C++, Fortran and Rust"?  

   project('polysnake', 'c', 'cpp', 'rust', 'fortran',
     default_options : ['cpp_std=c++14'],
     license : 'GPL3+')
   py3_mod = import('python3')
   py3_dep = dependency('python3')
   # Rust integration is not perfect.
   rustlib = static_library('func', 'func.rs')
   py3_mod.extension_module('polysnake',
     'polysnake.c',
     'func.cpp',
     'ffunc.f90',
     link_with : rustlib,
     dependencies : py3_dep)

|
| IDEs are supported by exporting to XCode+Visual Studio, and they
  provide their own interface (which a few less well known IDEs are
  starting to use).

Conan package manager
~~~~~~~~~~~~~~~~~~~~~

| There are several packaging tools for C these days, but one of the top
  contenders is `Conan <https://conan.io/>`__ (https://conan.io/).

   "Conan, the C / C++ Package Manager for Developers  The open source,
   decentralized and multi-platform package manager to create and share
   all your native binaries."

| What does a `CMake conan
  project <https://github.com/conan-io/hello>`__ look like?
  (https://github.com/conan-io/hello)
| What does a `conan
  Meson <https://docs.conan.io/en/latest/reference/build_helpers/meson.html>`__
  project look like?
  (https://docs.conan.io/en/latest/reference/build_helpers/meson.html)

CMake
~~~~~

| "Modern CMake" is the build tool of choice for many C projects.
| Just don't read the official docs, or the official book - they're
  quite out of date.
| `An Introduction to Modern
  CMake <https://cliutils.gitlab.io/modern-cmake/>`__
  (https://cliutils.gitlab.io/modern-cmake/)
| `CGold: The Hitchhiker’s Guide to the
  CMake <https://cgold.readthedocs.io/en/latest/>`__
  (https://cgold.readthedocs.io/en/latest/)

   "`CMake <https://cgold.readthedocs.io/en/latest/glossary/CMake.html#id1>`__
   is a meta build system. It can generate real `native build
   tool <https://cgold.readthedocs.io/en/latest/glossary/Native-build-tool.html#id1>`__
   files from abstracted text configuration. Usually such code lives in
   ``CMakeLists.txt`` files."

|
| Around 2015-2016 a bunch of IDEs got support for CMake: `Microsoft
  Visual
  Studio <https://blogs.msdn.microsoft.com/vcblog/2016/10/05/cmake-support-in-visual-studio/>`__,
  `CLion <https://blog.jetbrains.com/clion/2015/04/cmake-support-in-clion/>`__,
  `QtCreator <https://blog.qt.io/blog/2016/11/15/cmake-support-in-qt-creator-and-elsewhere/>`__,
  `KDevelop <https://userbase.kde.org/KDevelop4/Manual/Getting_started:_A_small_CMake_tutorial>`__,
  and `Android Studio
  (NDK) <https://developer.android.com/ndk/guides/cmake.html>`__. And a
  lot of people tried extra hard to like it, and a lot of C projects
  started supporting it.
| Apart from wide IDE support, it is also supported quite well by
  package managers like VCPkg and Conan.

Interpreter and REPL
--------------------

| Usually C is compiled.
| `Bic <https://github.com/hexagonal-sun/bic>`__ is an interpreter for C
  (https://github.com/hexagonal-sun/bic).

================================================================================
|image2|
`bic <https://github.com/hexagonal-sun/bic>`__: A C interpreter and API explorer
================================================================================

|
| Additionally there is
  "`Cling <https://github.com/root-project/cling>`__" which is based on
  the LLVM infrastructure and can even do C++.
| https://github.com/root-project/cling

Testing coverage.
-----------------

| Tests let us know that some certain function is running ok. Which code
  do we still need to test?
| `gcov <https://gcc.gnu.org/onlinedocs/gcc/Gcov.html>`__\ ``,`` a tool
  you can use in conjunction with GCC to test code coverage in your
  programs.
| `lcov, <http://ltp.sourceforge.net/coverage/lcov.php>`__ LCOV is a
  graphical front-end for GCC's coverage testing tool gcov.
| Instructions from codecov.io on how to use it with C, and clang or
  gcc. (codecov.io is free for public open source repos).
| https://github.com/codecov/example-c
| Here's documentation for how CPython gets coverage results for C.
|  https://devguide.python.org/coverage/#measuring-coverage-of-c-code-with-gcov-and-lcov
| Here is the CPython Travis CI configuration they use.
| https://github.com/python/cpython/blob/master/.travis.yml#L69

::

       - os: linux
         language: c
         compiler: gcc
         env: OPTIONAL=true
         addons:
           apt:
             packages:
               - lcov
               - xvfb
         before_script:
           - ./configure
           - make coverage -s -j4
           # Need a venv that can parse covered code.
           - ./python -m venv venv
           - ./venv/bin/python -m pip install -U coverage
           - ./venv/bin/python -m test.pythoninfo
         script:
           # Skip tests that re-run the entire test suite.
           - xvfb-run ./venv/bin/python -m coverage run --pylib -m test --fail-env-changed -uall,-cpu -x test_multiprocessing_fork -x test_multiprocessing_forkserver -x test_multiprocessing_spawn -x test_concurrent_futures
         after_script:  # Probably should be after_success once test suite updated to run under coverage.py.
           # Make the `coverage` command available to Codecov w/ a version of Python that can parse all source files.
           - source ./venv/bin/activate
           - make coverage-lcov
           - bash > (curl -s https://codecov.io/bash)

|

Static analysis
---------------

   "Static analysis has not been helpful in finding bugs in SQLite. More
   bugs have been introduced into SQLite while trying to get it to
   compile without warnings than have been found by static analysis." --
   https://www.sqlite.org/testing.html

|
| According to David Wheeler in "How to Prevent the next Heartbleed"
  (https://dwheeler.com/essays/heartbleed.html#static-not-found the
  security problem with a logo, a website, and a marketing team) only
  one static analysis tool found the Heartbleed vulnerability before it
  was known. This tool is called CQual++. One reason for projects not
  using these tools is that they have been (and some still are) hard to
  use. The LLVM project only started using the clang static analysis
  tool on it's `own projects
  recently <http://lists.llvm.org/pipermail/cfe-dev/2019-August/063195.html>`__
  for example. However, since Heartbleed in 2014 tools have improved in
  both usability and their ability to detect issues.
| I think it's generally accepted that static analysis tools are
  incomplete, in that each tool does not guarantee detecting every
  problem or even always detecting the same issues all the time. Using
  multiple tools can therefore be said to find multiple different types
  of problems.

Compilers are kind of smart
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The most basic of static analysis tools are compilers themselves. Over
  the years they have been getting more and more tools which used to
  only be available in dedicated Static Analyzers and Lint tools.

   Variable shadowing and format-string mismatches can be detected
   reliably and quickly is because both gcc and clang do this detection
   as part of their regular compile. --  `Bruce
   Dawson <http://randomascii.wordpress.com/2013/09/09/vote-for-the-vc-improvements-that-matter/>`__

| Here we see two issues (which used to be) very common in C being
  detected by the two most popular C compilers themselves.
| Compiling code with gcc "``-Wall -Wextra -pedantic``" options catches
  quite a number of potential or actual problems
  (https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html). Other
  compilers check different things as well. So using multiple compilers
  with their warnings can find plenty of different types of issues for
  you.

Compiler warnings should be turned in errors on CI.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| By getting your errors down to zero on Continuous Integration there is
  less chance of new warnings being introduced that are missed in code
  review. There are problems with distributing your code with warnings
  turned into errors, so that should not be done.
| Some points for people implementing this:

-  ``-Werror`` can be used to turn warnings into errors
-  ``-Wno-error=unknown-pragmas``
-  should run only in CI, and not in the build by default. See
   `werror-is-not-your-friend <https://embeddedartistry.com/blog/2017/5/3/-werror-is-not-your-friend>`__
   (https://embeddedartistry.com/blog/2017/5/3/-werror-is-not-your-friend).
-  Use most recent gcc, and most recent clang (change two travis linux
   builders to do this).
-  first have to fix all the warnings (and hopefully not break something
   in the process).
-  consider adding extra warnings to gcc: ``"-Wall -Wextra -Wpedantic"``
   See `C
   tooling <http://renesd.blogspot.com/2019/09/post-modern-c-tooling.html>`__
-  Also the Microsoft compiler MSVC on Appveyor can be configured to
   treat warnings as errors. The ``/WX`` argument option treats all
   warnings as errors. See `MSVC warning
   levels <https://docs.microsoft.com/en-us/cpp/build/reference/compiler-option-warning-level?view=vs-2019>`__
-  For MSVC on Appveyor, ``/wdnnnn`` Suppresses the compiler warning
   that is specified by nnnn. For example, /wd4326 suppresses compiler
   warning C4326.

| If you run your code on different CPU architectures, these compilers
  can find even more issues. For example 32bit/64bit Big Endian, and
  Little Endian.

Static analysis tool overview.
------------------------------

| Static analysis can be much slower than the analysis usually provided
  by compilation with gcc and clang. It trades off more CPU time for
  (hopefully) better results.
| `cppcheck <http://cppcheck.sourceforge.net/>`__ focuses of low false
  positives and can find many actual problems.
| `Coverity <https://www.coverity.com/>`__, a commercial static
  analyzer, free for open source developers
  `CppDepend <http://www.cppdepend.com/>`__, a commercial static
  analyzer based on Clang
  `codechecker <https://github.com/Ericsson/codechecker>`__,
  https://github.com/Ericsson/codechecker
| `cpplint <https://github.com/cpplint/cpplint>`__, Cpplint is a
  command-line tool to check C/C++ files for style issues following
  `Google's C++ style
  guide <http://google.github.io/styleguide/cppguide.html>`__.
| `Awesome static
  analysis <https://github.com/mre/awesome-static-analysis#cc>`__, a
  page full of static analysis tools for C/C++.
  https://github.com/mre/awesome-static-analysis#cc
| `PVS-Studio <https://www.viva64.com/en/pvs-studio/>`__, a commercial
  static analyzer, free for open source developers.

The Clang Static Analyzer
~~~~~~~~~~~~~~~~~~~~~~~~~

| `The Clang Static Analyzer <http://clang-analyzer.llvm.org/>`__
  (http://clang-analyzer.llvm.org/) is a free to use static analyzer
  that is quite high quality.

   The Clang Static Analyzer is a source code analysis tool that finds
   bugs in C, C++, and Objective-C programs. Currently it can be run
   either as a standalone tool or within Apple Xcode. The standalone
   tool is invoked from the command line, and is intended to be run in
   tandem with a build of a codebase.

| The talk "Clang Static Analysis"
  (https://www.youtube.com/watch?v=UcxF6CVueDM) talks about an LLVM tool
  called codechecker (https://github.com/Ericsson/codechecker).
| On MacOS an up to date scan-build and scan-view is included with the
  ``brew install llvm``.

::

   $SCANBUILD=`ls /usr/local/Cellar/llvm/*/bin/scan-build`
   $SCANBUILD -V python3 setup.py build

|
| On Ubuntu you can install scan-view with
  ``apt-get install clang-tools.``

cppcheck 
~~~~~~~~~

   Cppcheck is an analysis tool for C/C++ code. It provides unique code
   analysis to detect bugs and focuses on detecting undefined behaviour
   and dangerous coding constructs. The goal is to detect only real
   errors in the code (i.e. have very few false positives).

|
| The quote below was particularly interesting to me because it echos
  the sentiments of other developers, that testing will find more bugs.
  But here is one of the static analysis tools saying so as well.

   "You will find more bugs in your software by testing your software
   carefully, than by using Cppcheck."

| **To Install cppcheck:** http://cppcheck.sourceforge.net/ and
  https://github.com/danmar/cppcheck
| The manual can be found here: http://cppcheck.net/manual.pdf

::

   brew install cppcheck bear
   sudo apt-get install cppcheck bear

| **To run cppcheck on C code:** You can use
  `bear <https://github.com/rizsotto/Bear>`__ (the build ear) tool to
  record a compilation database (compile_commands.json). cppcheck can
  then know what c files and header files you are using.

::

   # call your build tool, like `bear make` to record.
   # See cppcheck manual for other C environments including Visual Studio.
   bear python setup.py build
   cppcheck --quiet --language=c --enable=all -D__x86_64__ -D__LP64__ --project=compile_commands.json

|
|  It does seem to find some errors, and style improvements that other
  tools do not suggest. Note that you can control the level of issues
  found to errors, to portability and style issues plus more. See
  ``cppcheck --help`` and the manual for more details about ``--enable``
  options.
| For example these ones from the pygame code base:

::

   [src_c/math.c:1134]: (style) The function 'vector_getw' is never used.
   [src_c/base.c:1309]: (error) Pointer addition with NULL pointer.
   [src_c/scrap_qnx.c:109]: (portability) Assigning a pointer to an integer is not portable.
   [src_c/surface.c:832] -> [src_c/surface.c:819]: (warning) Either the condition '!surf' is redundant or there is possible null pointer dereference: surf.

|

/Analyze in Microsoft Visual Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Visual studio by Microsoft can do static code analysis too. (
  https://docs.microsoft.com/en-us/visualstudio/code-quality/code-analysis-for-c-cpp-overview?view=vs-2017)
| "Using SAL annotations to reduce code defects."
  (https://docs.microsoft.com/en-us/visualstudio/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects?view=vs-2019)

   "In GNU C and C++, you can use function attributes to specify certain
   function properties that may help the compiler optimize calls or
   check code more carefully for correctness."

| https://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html

Custom static analysis for API usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Probably one of the most useful parts of static analysis is being able
  to write your own checks. This allows you to do checks specific to
  your code base in which general checks will not work. One example of
  this is the `gcc
  cpychecker <https://gcc-python-plugin.readthedocs.io/en/latest/cpychecker.html>`__
  (https://gcc-python-plugin.readthedocs.io/en/latest/cpychecker.html).
  With this, gcc can find API usage issues within CPython extensions
  written in C. Including reference counting bugs, and NULL pointer
  de-references, and other types of issues. You can write custom
  checkers with LLVM as well in the "`Checker Developer
  Manual <https://clang-analyzer.llvm.org/checker_dev_manual.html>`__"
  (https://clang-analyzer.llvm.org/checker_dev_manual.html)
| There is a list of `GCC plugins <https://gcc.gnu.org/wiki/plugins>`__
  (https://gcc.gnu.org/wiki/plugins) among them are some Linux security
  plugins by
  `grsecurity <https://www.grsecurity.net/features.php#tabs-gcc>`__.

Runtime checks and Dynamic Verification
---------------------------------------

| Dynamic verification tools examine code whilst it is running. By
  running your code under these dynamic verification tools you can help
  detect bugs. Either by testing manually, or by running your automated
  tests under the watchful eye of these tools. Runtime dynamic
  verification tools can detect certain errors that static analysis
  tools can't.
| Some of these tools are quite easy to add to a build in Continuous
  Integration(CI). So you can run your automated tests with some extra
  dynamic runtime verification enabled.
| Take a look at how easy they are to use?

   ::

      ./configure CFLAGS="-fsanitize=address,undefined -g" LDFLAGS="-fsanitize=address,undefined"
      make
      make check

|

Address Sanitizer
~~~~~~~~~~~~~~~~~

| Doing a test run with an address sanitizer apparently helps to detect
  various types of bugs.

   `AddressSanitizer <https://clang.llvm.org/docs/AddressSanitizer.html>`__
   is a fast memory error detector. It consists of a compiler
   instrumentation module and a run-time library. The tool can detect
   the following types of bugs:

-  Out-of-bounds accesses to heap, stack and globals
-  Use-after-free
-  Use-after-return (runtime flag
   ASAN_OPTIONS=detect_stack_use_after_return=1)
-  Use-after-scope (clang flag -fsanitize-address-use-after-scope)
-  Double-free, invalid free
-  Memory leaks (experimental)

| How to compile a python C extension with clang on MacOS:

::

   LDFLAGS="-g -fsanitize=address" CFLAGS="-g -fsanitize=address -fno-omit-frame-pointer" python3 setup.py install

|

Undefined Behaviour Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| From https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html

   `UndefinedBehaviorSanitizer
   (UBSan) <https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html>`__
   is a fast undefined behavior detector. UBSan modifies the program at
   compile-time to catch various kinds of undefined behavior during
   program execution, for example:

-  Using misaligned or null pointer
-  Signed integer overflow
-  Conversion to, from, or between floating-point types which would
   overflow the destination

| You can use the Undefined Behaviour Sanitizer with clang and gcc. Here
  is the `gcc documentation for Instrumentation Options and
  UBSAN <https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html>`__
  (https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html).
|  
| From https://www.sqlite.org/testing.html

   To help ensure that SQLite does not make use of undefined or
   implementation defined behavior, the test suites are rerun using
   instrumented builds that try to detect undefined behavior. For
   example, test suites are run using the "-ftrapv" option of GCC. And
   they are run again using the "-fsanitize=undefined" option on Clang.
   And again using the "/RTC1" option in MSVC

| To compile a python C extension with a UBSAN with clang on Mac do:

::

   LDFLAGS="-g -fsanitize=undefined" CFLAGS="-g -fsanitize=undefined -fno-omit-frame-pointer" python3 setup.py install

|

Microsoft Visual Studio Runtime Error Checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The Microsoft Visual Studio compiler can use the Run Time Error Checks
  feature to find some issues. `/RTC (Run-Time Error
  Checks) <https://docs.microsoft.com/en-us/cpp/build/reference/rtc-run-time-error-checks?view=vs-2019>`__
  (https://docs.microsoft.com/en-us/cpp/build/reference/rtc-run-time-error-checks?view=vs-2019)
| From `How to: Use Native Run-Time
  Checks <https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-use-native-run-time-checks?view=vs-2019>`__
  (`https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-use-native-run-time-checks?view=vs-2019) <https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-use-native-run-time-checks?view=vs-2019>`__

   -  Stack pointer corruption.
   -  Overruns of local arrays.
   -  Stack corruption.
   -  Dependencies on uninitialized local variables.
   -  Loss of data on an assignment to a shorter variable.

|

App Verifier
~~~~~~~~~~~~

   "Any Windows developers that are listening to this: **if you’re not
   using App Verifier, you are making a mistake**." -- Bruce Dawson

| Stangely App Verifier does not have very good online documentation.
  The best article available online about it is: `Increased Reliability
  Through More
  Crashes <https://randomascii.wordpress.com/2011/12/07/increased-reliability-through-more-crashes/>`__
  (https://randomascii.wordpress.com/2011/12/07/increased-reliability-through-more-crashes/)

   Application Verifier (AppVerif.exe) is a *dynamic verification* tool
   for user-mode applications. This tool monitors application actions
   while the application runs, subjects the application to a variety of
   stresses and tests, and generates a report about potential errors in
   application execution or design.

| https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/application-verifier
| https://docs.microsoft.com/en-us/windows/win32/win7appqual/application-verifier
| https://docs.microsoft.com/en-us/security-risk-detection/concepts/application-verifier

-  Buffer over runs
-  Use after free issues
-  Thread issues including using TLS properly.
-  Low resource handling
-  Race conditions

| If you have a memory corruption bug, App Verifier might be able to
  help you find it. If you are using Windows APIs wrong, have some
  threading issues, want to make sure you app runs under harsh
  conditions -- App Verifier might help you find it.
| Related to App Verifier is the
  `PageHeap <https://support.microsoft.com/en-us/help/286470/how-to-use-pageheap-exe-in-windows-xp-windows-2000-and-windows-server>`__
  tool(https://support.microsoft.com/en-us/help/286470/how-to-use-pageheap-exe-in-windows-xp-windows-2000-and-windows-server)
  It helps you find memory heap corruptions on Windows.

Performance profiling and measurement
-------------------------------------

   “The objective (not always attained) in creating high-performance
   software is to make the software able to carry out its appointed
   tasks so rapidly that it responds instantaneously, as far as the user
   is concerned.”  Michael Abrash. “Michael Abrash’s Graphics
   Programming Black Book.”

| Reducing energy usage, and run time requirements of apps can often be
  a requirement or very necessary. For a mobile or embedded application
  it can mean the difference of being able to run the program at all.
  Performance can directly be related to user happiness but also to the
  financial performance of a piece of software.
| But how to we measure the performance of a program, and how to we know
  what parts of a program need improvement? Tooling can help.

Valgrind
~~~~~~~~

| Valgrind has its own section here because it does lots of different
  things for us. It's a great tool, or set of tools for improving your
  programs. It used to be available only on linux, but is now also
  available on MacOS.
| Apparently Valgrind would have caught the heartbleed issue if it was
  used with a fuzzer.
| http://valgrind.org/docs/manual/quick-start.html

Apple Performance Tools
~~~~~~~~~~~~~~~~~~~~~~~

| Apple provides many `performance related development
  tools <https://developer.apple.com/library/archive/documentation/Performance/Conceptual/PerformanceOverview/PerformanceTools/PerformanceTools.html>`__.
  Along with the gcc and llvm based tools, the main tool is called
  `Instruments <https://help.apple.com/instruments/mac/current/>`__.
  Instruments (part of Xcode) allows you to record and analyse programs
  for lots of different aspects of performance - including graphics,
  memory activity, file system, energy and other program events. By
  being able to record and analyse different types of events together
  can make it convienient to find performance issues.

LLVM performance tools.
~~~~~~~~~~~~~~~~~~~~~~~

| Many of the low level parts of the tools in XCode are made open source
  through the LLVM project. See "LLVM Machine Code Analyzer" (
  https://llvm.org/docs/CommandGuide/llvm-mca.html) as one example. See
  the `LLVM XRay
  instrumentation <https://llvm.org/docs/XRayExample.html>`__
  (https://llvm.org/docs/XRayExample.html).
| There's also an interesting talk on XRay here "`XRay in LLVM: Function
  Call Tracing and
  Analysis <https://www.youtube.com/watch?v=jyL-__zOGcU>`__"
  (https://www.youtube.com/watch?v=jyL-__zOGcU) by *Dean Michael
  Berris.*

GNU/Linux tools
~~~~~~~~~~~~~~~

|

Microsoft performance tools.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

Intel performance tools.
~~~~~~~~~~~~~~~~~~~~~~~~

| https://software.intel.com/en-us/vtune

Caching builds
--------------

| https://ccache.samba.org/
| ccache is very useful for reducing the compile time of large C
  projects. Especially when you are doing a 'rebuild from scratch'. This
  is because ccache can cache the compilation of parts in this situation
  when the files do not change.
| http://itscompiling.eu/2017/02/19/speed-cpp-compilation-compiler-cache/
| This is also useful for speeding up CI builds, and especially when
  large parts of the code base rarely change.

Distributed building.
---------------------

|
| distcc https://github.com/distcc/distcc
| icecream https://github.com/icecc/icecream

Complexity of code.
-------------------

   "Complex is better than complicated. It's OK to build very complex
   software, but you don't have to build it in a complicated way. Lizard
   is a free open source tool that analyse the complexity of your source
   code right away supporting many programming languages, without any
   extra setup. It also does code clone / copy-paste detection."

| Lizard is a modern complexity command line tool,
| that also has a website UI: http://www.lizard.ws/
| https://github.com/terryyin/lizard

   # install lizard
   python3 -m pip install lizard
   # show warnings only and include/exclude some files.
   lizard src_c/ -x"src_c/_sdl2*" -w 

..

   # Can also run it as a python module.
   python3 -m lizard src_c/ -x"src_c/_sdl2*" -w
   # Show a full report, not just warnings (-w).
   lizard src_c/ -x"src_c/_sdl2*" -x"src_c/_*" -x"src_c/SDL_gfx*"
   -x"src_c/pypm.c"

|
| Want people to understand your code? Want Static Analyzers to
  understand your code better? Want to be able to test your code more
  easily? Want your code to run faster because of less branches? Then
  **you may want to find complicated code and refactor it**.

==========================================================
|image3|
Lizard can also make a pretty word cloud from your source.
==========================================================

|
| Lizard complexity analysis can be run in Continuous Integration (CI).
  You can also give it lists of functions to ignore and skip if you
  can't refactor some function right away. Perhaps you want to stop new
  complex functions from entering your codebase? To stop new complex
  functions via CI make a supression list of all the current warnings
  and then make your CI use that and fail if there are new warnings.

Testing your code on different OS/architectures.
------------------------------------------------

| Sometimes you need to be able to fix an issue on an OS or architecture
  that you don't have access to. Luckily these days there are many tools
  available to quickly use a different system through emulation, or
  container technology.
| Vagrant
| Virtualbox
| Docker
| Launchpad, compile and run tests on many architectures.
| Mini cloud (ppc machines for debugging)
| If you pay Travis CI, they allow you to connect to the testing host
  with ssh when a test fails.

Code Formatting
---------------

| clang-format
| clang-format - rather than manually fix various formatting errors
  found with a linter, many projects are just using clang-format to
  format the code into some coding standard.

Services
--------

| LGTM is an 'automated code review tool' with github (and other code
  repos) support. https://lgtm.com/help/lgtm/about-automated-code-review
| Coveralls provides a store for test coverage results with github (and
  other code repos) support. https://coveralls.io/

Coding standards for C
----------------------

| There are lots of coding standards for C, and there are tools to check
  them.
| An older set of standards is the
  `MISRA_C <https://en.wikipedia.org/wiki/MISRA_C>`__
  (https://en.wikipedia.org/wiki/MISRA_C) aims to facilitate code
  safety, security, and portability for embedded systems.
| The `Linux Kernel Coding
  standard <https://www.kernel.org/doc/html/v4.10/process/coding-style.html>`__
  (https://www.kernel.org/doc/html/v4.10/process/coding-style.html) is
  well known mainly because of the popularity of the Linux Kernel. But
  this is mainly concerned with readability.
| A newer one is the `CERT C coding
  standard <https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards>`__
  (https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards),
  and it is a secure coding standard (not a safety one).
| The website for the CERT C coding standard is quite amazing. It links
  to tools that can detect each of the problems automatically (when they
  can be). It is very well researched, and links each problem to other
  relevant standards, and gives issues priorities. A good video to watch
  on CERT C is "`How Can I Enforce the SEI CERT C Coding Standard Using
  Static Analysis? <https://www.youtube.com/watch?v=awY0iJOkrg4>`__"
  (https://www.youtube.com/watch?v=awY0iJOkrg4). They do releases of the
  website, which is edited as a wiki. At the time of writing the last
  release into book form was in 2016.

How are other projects tested?
------------------------------

| We can learn a lot by how other C projects are going about their
  business today.
| Also, thanks to CI testing tools defining things in code we can see
  how automated tests are run on services like Travis CI and Appveyor.

SQLite
~~~~~~

| "`How SQLite Is Tested <https://www.sqlite.org/testing.html>`__"

Curl
~~~~

| "`Testing
  Curl <https://daniel.haxx.se/blog/2017/10/12/testing-curl/>`__"
| https://github.com/curl/curl/blob/master/.travis.yml

Python
~~~~~~

| "`How is CPython
  tested? <https://discuss.python.org/t/how-is-cpython-tested/2256>`__"
| https://github.com/python/cpython/blob/master/.travis.yml

OpenSSL
~~~~~~~

| "`How is OpenSSL
  tested? <https://github.com/openssl/openssl/issues/9831>`__"
| https://github.com/openssl/openssl/blob/master/.travis.yml
| They use Coverity too: https://github.com/openssl/openssl/pull/9805
| https://github.com/openssl/openssl/blob/master/fuzz/README.md

libsdl
~~~~~~

| "`How is SDL
  tested? <https://discourse.libsdl.org/t/how-is-sdl-tested/26576>`__"
  [No response]

Linux
~~~~~

| https://stackoverflow.com/questions/3177338/how-is-the-linux-kernel-tested\ https://www.linuxjournal.com/content/linux-kernel-testing-and-debugging

Haproxy
~~~~~~~

| https://github.com/haproxy/haproxy/blob/master/.travis.yml
| There is some discussion of `Post Modern C
  Tooling <https://www.reddit.com/r/C_Programming/comments/dey8bq/post_modern_c_tooling/>`__
  on the "C_Programming" reddit forum.


.. |image0| image:: https://1.bp.blogspot.com/-vynRQ-xMFHc/XcKg6mKOITI/AAAAAAAABhE/9aWuVKDJoH43V81NYYD_YtBdXQ_RT58cwCEwYBhgL/s320/the-c-programming-language-scan.png
   :width: 306px
   :height: 320px
   :target: https://1.bp.blogspot.com/-vynRQ-xMFHc/XcKg6mKOITI/AAAAAAAABhE/9aWuVKDJoH43V81NYYD_YtBdXQ_RT58cwCEwYBhgL/s1600/the-c-programming-language-scan.png
.. |image1| image:: https://1.bp.blogspot.com/-nQTQVBBJgw4/XZjCZxMjF0I/AAAAAAAABeE/rCn_FdXAqHYrVjoWPHy3GV_1pBFYTje6gCLcBGAsYHQ/s320/cgdb_debugging.png
   :width: 320px
   :height: 313px
   :target: https://1.bp.blogspot.com/-nQTQVBBJgw4/XZjCZxMjF0I/AAAAAAAABeE/rCn_FdXAqHYrVjoWPHy3GV_1pBFYTje6gCLcBGAsYHQ/s1600/cgdb_debugging.png
.. |image2| image:: https://1.bp.blogspot.com/-6LlMqD4soX4/XZxrf7HnFPI/AAAAAAAABeg/W_9ex_MAoDcIwYW8G69M_l4O-KcclF2lwCLcBGAsYHQ/s320/c-interpreter-hello-world.gif
   :width: 320px
   :height: 233px
   :target: https://1.bp.blogspot.com/-6LlMqD4soX4/XZxrf7HnFPI/AAAAAAAABeg/W_9ex_MAoDcIwYW8G69M_l4O-KcclF2lwCLcBGAsYHQ/s1600/c-interpreter-hello-world.gif
.. |image3| image:: https://1.bp.blogspot.com/-5P23Xf1TqJw/XZdW7jzAXfI/AAAAAAAABdY/HyOtqgoZSW8J0zQjjheN3NsSkSjom7rWgCLcBGAsYHQ/s320/pygame_C_word_cloud.png
   :width: 320px
   :height: 319px
   :target: https://1.bp.blogspot.com/-5P23Xf1TqJw/XZdW7jzAXfI/AAAAAAAABdY/HyOtqgoZSW8J0zQjjheN3NsSkSjom7rWgCLcBGAsYHQ/s1600/pygame_C_word_cloud.png
