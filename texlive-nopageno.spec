Name:		texlive-nopageno
Version:	18128
Release:	2
Summary:	No page numbers in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nopageno
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX's standard styles use two page styles, one on normal
pages and one on 'opening' pages with \maketitle or \chapter,
etc. Unfortunately there is only easy access to changing one of
these two so if you want something other than 'plain' on the
opening pages you must use \thispagestyle on each such page.
The fancyhdr package does provide a more flexible interface,
but if you just want an empty page style on all pages then this
package will do the job.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nopageno/nopageno.sty
%doc %{_texmfdistdir}/doc/latex/nopageno/nopageno.pdf
%doc %{_texmfdistdir}/doc/latex/nopageno/nopageno.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
