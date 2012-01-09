# revision 24981
# category Package
# catalog-ctan /macros/latex/contrib/hhtensor
# catalog-date 2011-12-29 22:44:25 +0100
# catalog-license lppl
# catalog-version 0.61
Name:		texlive-hhtensor
Version:	0.61
Release:	1
Summary:	Print vectors, matrices, and tensors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hhtensor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for vectors, matrices, and
tensors with different styles -- arrows (as the LaTeX default),
underlined, and bold).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hhtensor/hhtensor.sty
%doc %{_texmfdistdir}/doc/latex/hhtensor/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hhtensor/Makefile
%doc %{_texmfdistdir}/doc/latex/hhtensor/README
%doc %{_texmfdistdir}/doc/latex/hhtensor/getversion.tex
%doc %{_texmfdistdir}/doc/latex/hhtensor/hhtensor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hhtensor/hhtensor.dtx
%doc %{_texmfdistdir}/source/latex/hhtensor/hhtensor.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
