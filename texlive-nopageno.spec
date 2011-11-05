# revision 18128
# category Package
# catalog-ctan /macros/latex/contrib/nopageno
# catalog-date 2010-05-11 12:36:30 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-nopageno
Version:	20100511
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX's standard styles use two page styles, one on normal
pages and one on 'opening' pages with \maketitle or \chapter,
etc. Unfortunately there is only easy access to changing one of
these two so if you want something other than 'plain' on the
opening pages you must use \thispagestyle on each such page.
The fancyhdr package does provide a more flexible interface,
but if you just want an empty page style on all pages then this
package will do the job.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nopageno/nopageno.sty
%doc %{_texmfdistdir}/doc/latex/nopageno/nopageno.pdf
%doc %{_texmfdistdir}/doc/latex/nopageno/nopageno.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
