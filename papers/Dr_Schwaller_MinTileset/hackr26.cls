% BUILD-ONLY STAND-IN for the missing hackr26.cls (article, 10pt, 1in margins).
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hackr26}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{caption,graphicx,amssymb,amsmath,amsthm}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{cor}{Corollary}
\newtheorem{obs}{Observation}
\newtheorem{conj}{Conjecture}
\newtheorem{prop}{Proposition}
\newtheorem{invar}{Invariant}
\theoremstyle{definition}\newtheorem{defini}{Definition}
\endinput
