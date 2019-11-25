---
title: Project Title
subtitle: Class, Term
author: Author Name
date: Date
geometry: margin=0.75in
fontsize: 11pt
---

# Introduction

This is how you use a reference when mentioning a paper [@littman1994markov]. They need to be in `library.bib`, in the right format, which is easiest to get if you search the title on Google scholar, click the double quotation icon after the search result, then click the BibTeX link at the bottom.

If you need, you can use inline math formulas (LaTeX syntax), such as this: $P_t = x_t^2 + x_t$, or have them larger on their own line:

$$R_t = \alpha \frac{P_t}{x_t}$$

For plotting, it's best to include PDF's as they look good at any zoom level. This is a full width plot:

![](../plots/experiment_1.pdf){width=100%}

And here are two side by side:

![](../plots/experiment_2.pdf){width=50%}\ ![](../plots/experiment_2.pdf){width=50%}

You can also add tables:

|             | Input value | Output result |
| ----------- | :---------: | ------------: |
| Iteration 1 |      5      |            25 |
| Iteration 2 |     16      |           256 |
| Iteration 3 |      1      |             1 |

<!---
The colons indicate alignment (`|---|` means left, `|---:|` means right, and `|:---:|` center).
-->

The used references will be automatically added at the end of your paper, so you can add a _References_ heading if you like.

# References
