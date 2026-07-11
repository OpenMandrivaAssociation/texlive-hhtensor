%global tl_name hhtensor
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.61
Release:	%{tl_revision}.1
Summary:	Print vectors, matrices, and tensors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hhtensor
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hhtensor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for vectors, matrices, and tensors with
different styles -- arrows (as the LaTeX default), underlined, and bold.

