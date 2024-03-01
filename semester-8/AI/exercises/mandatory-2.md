---
title: "Mandatory 2"
author: Albert Rise Nielsen (albn@itu.dk)
header-includes: |
    \usepackage{pdfpages}
    \DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}
---

## 1)
Following is the pseudo code for the minimax algorithm.
```
function EXPECTIMINIMAX-SEARCH(state) returns an action
    value, move <- MAX-VALUE(state)
    return move

function MAX-VALUE(state) returns (utility,move)
    if IS-TERMINAL(state) then
        return UTILITY(state), null
    v <- -∞
    for each a in ACTIONS(state) do
        v2,a2 <- CHANCE-VALUE(MIN-VALUE, RESULT(state,a))
        if v2 > v then
            v,move <- v2,a
    return v,move

function MIN-VALUE(state) returns (utility,move)
    if IS-TERMINAL(state) then
        return UTILITY(state), null
    v <- ∞
    for each a in ACTIONS(state) do
        v2,a2 <- CHANCE-VALUE(MAX-VALUE, RESULT(state,a))
        if v2 < v then
            v,move ← v2,a
    return v,move

function CHANCE-VALUE(next, state) returns (utility, move)
    if IS-TERMINAL(state) then
        return UTILITY(state), null
    v <- 0
    for each r in ACTIONS(state) do
        v2,a2 <- next(RESULT(state,r))
        v <- v + (P(r) * v2)
    return v, null
```

## 2)

The full game tree can be seen in the following image, where the best decision for max to start with is marked with a thicker green arrow. Max wil place their token in the lower left corner to optimize their chance of winning the game.

\newpage
\begin{figure}
    \centering
    \includepdf[pages=-,angle=90]{./out/mandatory-2-2/mandatory-2-2.pdf}
\end{figure}

