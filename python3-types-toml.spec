Summary:	Typing stubs for toml
Summary(pl.UTF-8):	Zaślepki typów dla modułu toml
Name:		python3-types-toml
Version:	0.10.8.7
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/types-toml/
Source0:	https://files.pythonhosted.org/packages/source/t/types-toml/types-toml-%{version}.tar.gz
# Source0-md5:	9a35470257ab36a63d6d28449f9f0584
URL:		https://pypi.org/project/types-toml/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEP 561 type stub package for the toml package. It can be
used by type-checking tools like mypy, pyright, pytype, PyCharm, etc.
to check code that uses toml.

%description -l pl.UTF-8
Zgodny z PEP 561 pakiet zaślepek typów dla pakietu toml. Może być
używany przez narzędzia sprawdzające typy, takie jak mypy, pyright,
pytype, PyCharm itp. do sprawdzania kodu wykorzystującego bibliotekę
toml.

%prep
%setup -q -n types-toml-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md 
%{py3_sitescriptdir}/toml-stubs
%{py3_sitescriptdir}/types_toml-%{version}-py*.egg-info
