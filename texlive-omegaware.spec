Name:		texlive-omegaware
Version:	20111102
Release:	1
Summary:	TeXLive omegaware package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/omegaware.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/omegaware.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-omegaware.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive omegaware package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/odvicopy.1*
%doc %{_texmfdir}/doc/man/man1/odvicopy.man1.pdf
%doc %{_texmfdir}/doc/man/man1/odvips.man1.pdf
%doc %{_mandir}/man1/odvitype.1*
%doc %{_texmfdir}/doc/man/man1/odvitype.man1.pdf
%doc %{_mandir}/man1/ofm2opl.1*
%doc %{_texmfdir}/doc/man/man1/ofm2opl.man1.pdf
%doc %{_mandir}/man1/opl2ofm.1*
%doc %{_texmfdir}/doc/man/man1/opl2ofm.man1.pdf
%doc %{_mandir}/man1/otangle.1*
%doc %{_texmfdir}/doc/man/man1/otangle.man1.pdf
%doc %{_mandir}/man1/otp2ocp.1*
%doc %{_texmfdir}/doc/man/man1/otp2ocp.man1.pdf
%doc %{_mandir}/man1/outocp.1*
%doc %{_texmfdir}/doc/man/man1/outocp.man1.pdf
%doc %{_mandir}/man1/ovf2ovp.1*
%doc %{_texmfdir}/doc/man/man1/ovf2ovp.man1.pdf
%doc %{_mandir}/man1/ovp2ovf.1*
%doc %{_texmfdir}/doc/man/man1/ovp2ovf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
