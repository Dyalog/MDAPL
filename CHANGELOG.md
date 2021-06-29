# MDAPL Changelog

For the latest release of “Mastering Dyalog APL”, visit [https://github.com/Dyalog/MDAPL/releases](https://github.com/Dyalog/MDAPL/releases).

## v0.1

Version 0.1 includes a significant number of changes because
substantial work on the first chapters had already been done
when versioning of the MDAPL rework started.

 - Add chapter “Execute and Format Control”
   - make original Spe 2.2 a subsection on dyadic `⍕`;
   - specification `'E'` is next to _all other_ specifications (was Spe 2.3);
   - [n] Specialist's Section "Dyadic Execute" now mentions the left argument to `⍎` can be a reference to a namespace;
   - [n] section on `⎕FMT` now contains a quick reference to all specifications;
   - `'Kn'` listed as a qualifier for `⎕FMT` instead of a specification, which is now in agreement with the documentation (cf. [http://help.dyalog.com/latest/#Language/System%20Functions/Format%20Dyadic.htm#GFormat](http://help.dyalog.com/latest/#Language/System%20Functions/Format%20Dyadic.htm#GFormat));
   - [n] mention which qualifiers work with the specification `'G'`;
   - [n] remark that common `FORMAT ERROR` is the mixture of incompatible qualifiers/specifications;
   - [n] suggest not using `⍎` for weird programming tricks, instead use functions that receive arguments and return values;
   - [n] add section on controlling session output with user commands and the dfns namespace;