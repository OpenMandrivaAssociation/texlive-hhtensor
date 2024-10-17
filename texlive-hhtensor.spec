Name:		texlive-hhtensor
Version:	54080
Release:	2
Summary:	Print vectors, matrices, and tensors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hhtensor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
