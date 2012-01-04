# revision 18128
# category Package
# catalog-ctan /macros/latex/contrib/nopageno
# catalog-date 2010-05-11 12:36:30 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-nopageno
Version:	20100511
Release:	2
Summary:	No page numbers in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nopageno
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nopageno.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
