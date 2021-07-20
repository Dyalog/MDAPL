# MDAPL Changelog

For the latest release of “Mastering Dyalog APL”, visit [https://github.com/Dyalog/MDAPL/releases](https://github.com/Dyalog/MDAPL/releases).

This changelog keeps track of two types of changes.
In the first instance, it lists the changes between consecutive releases of this book.
However, because this book is a rework of the first edition by Bernard Legrand,
this changelog also marks with [n] content that is new in this rework.

## v0.2.0

 - Add chapter “Working on Data Shape”
   - [n] replace the "type" primitive (`∊` with `⎕ML ← 0`) with a reference to `⎕DR`;
   - [n] updated spec of take `↑` and drop `↓` because they now conform to leading axis theory (the length of the left argument now can be smaller than the rank of the right argument);
   - [n] include exercises to write expressions that determine `⍴ns↑array` and `⍴ns↓array` from `ns`, `≢ns`, and `⍴array`;
   - [n] include exercises to transform the left argument to take `↑` into a left argument for drop `↓` and vice-versa, given a fixed right argument;
   - [n] include more natural example of when _laminate_ is useful to "show vectors";
   - don't call _mirror_ to reverse `⌽` and reverse first `⊖`;
   - [n] include remark about `⊖` not being a no-op for vectors, although visually one might expect that;
   - regarding the solutions for the problems:
     - move them to the end of the chapter;
	 - [n] write them as dfns;
	 - [n] modernise some of the solutions;
	 - [n] include explanations of how to arrive at the solutions;

## v0.1.1

 - Fix issues #1, #3, and #4.
 - Fix other minor issues and typos.
 - [n] Add a row about shy results on the comparative table between dfns and tradfns.
 - Acknowledge contributions to this rework in the README file.

## v0.1.0

Version 0.1.0 includes a significant number of changes because
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
   
 - Add chapter “First-Aid Kit”
   - update debugging instructions for Windows;
   - [n] add debugging instructions for RIDE;
   - (possibly other changes);
   
 - Add chapter “User-Defined Functions”
   - reorder sections on tradfns and dfns to give more emphasis on dfns;
   - [n] add sections on dfns;
   - [n] add exercises on dfns;
   - [n] comparative table between dfns and tradfns;
   - (possibly other changes);
   
 - Add chapter “Some Primitive Functions”
   - introduce match and depth (≡) and not-match and tally (≢);
   - [n] mention unique that renders the `((⍳≢vector) = vector ⍳ vector) / vector` example as obsolete;
   - (possibly other changes);
   
 - Add chapter “Data and Variables”
   - (possibly other changes);
   
 - Add chaper “Getting Started”
   - [n] add instructions for Linux and MacOS users;
   - [n] add instructions for RIDE;
   - [n] add instructions for Jupyter notebooks;
   - [n] add more information on typing APL glyphs;
   - (possibly other changes);
   
 - Add chapter “Will You Play APL With Me?”
   - (possibly other changes);
   
 - Add chapter “Appendices”
   - [n] add appendix with all event numbers;
   - [n] add appendix with all the variables that are commonly used in the book and too long to type;
