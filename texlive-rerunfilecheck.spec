Name:		texlive-rerunfilecheck
Version:	63869
Release:	2
Summary:	Checksum based rerun checks on auxiliary files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rerunfilecheck
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rerunfilecheck.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rerunfilecheck.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rerunfilecheck.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides additional rerun warnings if some
auxiliary files have changed. It is based on MD5 checksum
provided by pdfTeX, LuaTeX, XeTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/rerunfilecheck
%{_texmfdistdir}/tex/latex/rerunfilecheck
%doc %{_texmfdistdir}/doc/latex/rerunfilecheck

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
