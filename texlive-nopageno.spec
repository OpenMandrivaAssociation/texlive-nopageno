%global tl_name nopageno
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	No page numbers in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nopageno
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX's standard styles use two page styles, one on normal pages and one
on 'opening' pages with \maketitle or \chapter, etc. Unfortunately there
is only easy access to changing one of these two so if you want
something other than 'plain' on the opening pages you must use
\thispagestyle on each such page. The fancyhdr package does provide a
more flexible interface, but if you just want an empty page style on all
pages then this package will do the job.

