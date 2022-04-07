# MDAPL Changelog

For the latest release of “Mastering Dyalog APL”, visit [https://github.com/Dyalog/MDAPL/releases](https://github.com/Dyalog/MDAPL/releases).

This changelog keeps track of two types of changes.
In the first instance, it lists the changes between consecutive releases of this book.
However, because this book is a rework of the first edition by Bernard Legrand,
this changelog also marks with [n] content that is new in this rework.

## 0.4.5

  - Moved source files into dedicated folder `docs`.
  - Simplified build process by removing resource migration.

## 0.4.4

  - Improve exercise presentation:
    - provide an admonition for exercises with auto-numbering;
    - provide an admonition for solutions;
    - link solutions to corresponding exercises;
  - Improve phrasing of several exercises and provide more concrete instructions.

## 0.4.3.1

  - Use local APL385 font when possible.

## 0.4.3

  - Stylistic improvements to online book:
    - now uses the APL385 Unicode font;
    - fixed improperly styled admonitions.
  - Unify “tip”/“advice”/“suggestion”/“recommendation”/etc admonitions as “tip”.
  - Fix `NameError` in preprocessing script.

## 0.4.2

  - Fix #24 by improving preprocessing script.
  - Improve formatting and wording in the chapter (fix #23 and #26).
  - Fix typos (fix #23).
  - Fix #21.

## 0.4.1

  - Fix typos.
  - Fix duplicate headers in “Some Primitive Functions”:
    - Under “Axis Specification”, there were 2 almost-consecutive duplicate level 4 headers under the _same_ level 3 header, and it made sense to join them together;
    - Rename “Special Notations” to “Replicate with Axis” under the section on replicate, to make the header more explicit;

## v0.4

  - Add chapter “Nested Arrays (Continued)”:
    - refactor “First Contact” > “More About DISPLAY” (see #13);
    - remove subsection “Depth” > “Match & Natch” (dyadic `≡` and `≢` are already covered earlier in the book);
    - [n] add subsection “Depth” > “The Depth of an Array, Take 2” (introduce default vector values technique; try fixing the issue with `Process` by giving default values to the missing positions of the argument vector);
    - [n] add section “Nest” (the function `Process` was used to introduce the concept of depth; we can use the same example to motivate monadic `⊆` as a way to do some "argument validation"):
        - [n] introduce `⊆` that encloses if the argument is simple;
        - [n] add subsection “Argument Homogenisation” (fixes the issue with `Process` by using `⊆`);
        - [n] add subsection “Nesting a Scalar” (explains why it may look like `⊆` "doesn't work" on simple scalars).
    - [n] establish the connection between mix with axis `↑[k]` and mix followed by dyadic transpose;
    - make a section out of the intermission exercises (so that they are easier to find in the table of contents of the chapter);
    - remove section “First & Type” (The “First” portion was moved to the section “Pick” and the “Type” portion was split into “Prototype, Fill Item” and the “Specialist's Section”);
    - refactor section “Prototype, Fill Item”:
        - rename it to “Type, Prototype, Fill Item” (before we introduce the notions of prototype and fill item, we define the type of an array); and
        - [n] define the type of an array in a descriptive manner (we can't just say that the type of `array` is `∊array` because `∊` is the enlist function).
    - refactor section “Pick”:
        - rename subsection “Beware!” to “Left Argument Length” (more descriptive name);
        - rename subsection “Important” to “Disclosed Result” (ditto);
        - take `]box` effects into consideration in subsections “Left Argument Length” and “Disclosed Result”; and
        - add subsection “Pick First”, containing the “First” portion of the old “First & Type” section.
    - refactor section “Partition & Partitioned Enclose”:
        - swap title order to match order of contents;
        - [n] introduce partitioned enclose `pattern ⊂ array` as a series of sub-subsections covering the several nuances of its behaviour; and
        - use the old subsection “The IBM Definition” as the introduction to partition `⊆`.
    - refactor section “Enlist” (remove references to `⎕ML`, as those were moved to the Specialist's Section);
    - refactor exercises:
        - [n] added exercise 7 to find the result of an empty partitioned enclose, like `0⊂'Partition'`;
        - [n] added exercise 8 using nest `⊆Y` for argument homogenisation;
    - refactor “The Specialist's Section”:
        - [n] add subsection "Computing the Type and Prototype" (after talking about `⎕ML`):
            - use `⊃0⍴⊂` / `∊` with `⎕ML ← 0` to figure out the type of an array;
            - use `⊃0⍴` / `∊⊃` with `⎕ML ← 0` to figure out the prototype of an array; and
            - [n] include recursive dfn to compute type when `⎕ML ≥ 0`.
        - refactor “The IBM Partition on Matrices”:
            - rename it to “High-rank Partition”;
            - [n] add remark about result similarity if `]box` is OFF;
            - point out main difference between `⊂` and `⊆` (`⊂` creates a vector of sub-arrays, while `⊆` creates a sub-array of vectors);
            - [n] add rules to characterise the result of a partition operation;
  - Include email address to where feedback/errata can be sent.
  - Update TOC format to comply with Jupyter Book's upgrade.
  - Fix styling issues with “Working on Data Shape” (a “rules” admonition and listing some matrices on the solutions for the exercises).

## v0.3

 - Add chapter “Special Syntax”:
   - change modified assignment variable names to "make more sense" out of context, and include example values;
   - [n] include a note saying that array notation could supersede the usage of `,←` to define long vectors;
   - [n] move the in-depth discussion about the disadvantages of not using parentheses in multiple assignment to this chapter, from the chapter “Data and Variables”;
   - [n] add enlist `∊` and table `⍪` to the list of primitives that work with selective assignment;
 - Add the selective assignment appendix to the appendices.

## v0.2.1

 - [n] Add example in “Data and Variables” that explains why multiple assignment without parenthesis can be ambiguous to read.
 - Do not call "mirror" to the primitives `⌽` and `⊖`.
 - Make text a bit less Windows-centric.
 - Format APL terms consistently throughout the book (with italics only).
 - Prefer "catenate" over "concatenate" for the primitive `,`.
 - Prefer the construct "the function <name>" over "the <name> function" – the "function" qualifier before the function name makes it clearer, earlier, that we are talking about a specific function.
 - Fix reference issues with images that had empty captions.

## v0.2.0

 - Add chapter “Working on Data Shape”:
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

 - Add chapter “Execute and Format Control”:
   - make original Spe 2.2 a subsection on dyadic `⍕`;
   - specification `'E'` is next to _all other_ specifications (was Spe 2.3);
   - [n] Specialist's Section "Dyadic Execute" now mentions the left argument to `⍎` can be a reference to a namespace;
   - [n] section on `⎕FMT` now contains a quick reference to all specifications;
   - `'Kn'` listed as a qualifier for `⎕FMT` instead of a specification, which is now in agreement with the documentation (cf. [http://help.dyalog.com/latest/#Language/System%20Functions/Format%20Dyadic.htm#GFormat](http://help.dyalog.com/latest/#Language/System%20Functions/Format%20Dyadic.htm#GFormat));
   - [n] mention which qualifiers work with the specification `'G'`;
   - [n] remark that common `FORMAT ERROR` is the mixture of incompatible qualifiers/specifications;
   - [n] suggest not using `⍎` for weird programming tricks, instead use functions that receive arguments and return values;
   - [n] add section on controlling session output with user commands and the dfns namespace;
   
 - Add chapter “First-Aid Kit”:
   - update debugging instructions for Windows;
   - [n] add debugging instructions for RIDE;
   - (possibly other changes);
   
 - Add chapter “User-Defined Functions”:
   - reorder sections on tradfns and dfns to give more emphasis on dfns;
   - [n] add sections on dfns;
   - [n] add exercises on dfns;
   - [n] comparative table between dfns and tradfns;
   - (possibly other changes);
   
 - Add chapter “Some Primitive Functions”:
   - introduce match and depth (≡) and not-match and tally (≢);
   - [n] mention unique that renders the `((⍳≢vector) = vector ⍳ vector) / vector` example as obsolete;
   - (possibly other changes);
   
 - Add chapter “Data and Variables”:
   - (possibly other changes);
   
 - Add chaper “Getting Started”:
   - [n] add instructions for Linux and MacOS users;
   - [n] add instructions for RIDE;
   - [n] add instructions for Jupyter notebooks;
   - [n] add more information on typing APL glyphs;
   - (possibly other changes);
   
 - Add chapter “Will You Play APL With Me?”:
   - (possibly other changes);
   
 - Add chapter “Appendices”:
   - [n] add appendix with all event numbers;
   - [n] add appendix with all the variables that are commonly used in the book and too long to type;
