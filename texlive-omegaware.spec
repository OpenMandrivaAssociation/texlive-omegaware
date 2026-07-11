%global tl_name omegaware
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A wide-character-set extension of TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/systems/omega
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/omegaware.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/omegaware.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(omegaware.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A development of TeX, which deals in multi-octet Unicode characters, to
enable native treatment of a wide range of languages without changing
character-set. Work on Omega has ceased (the TeX Live package contains
only support files); its compatible successor is aleph, which is itself
also in major maintenance mode only. Ongoing projects developing Omega
(and Aleph) ideas include Omega-2 and LuaTeX.

