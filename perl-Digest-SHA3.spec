#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-SHA3
Version  : 1.05
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA3-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA3-1.05.tar.gz
Summary  : Perl extension for SHA-3
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Digest-SHA3-bin = %{version}-%{release}
Requires: perl-Digest-SHA3-man = %{version}-%{release}
Requires: perl-Digest-SHA3-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Digest::SHA3 version 1.05
=========================
Digest::SHA3 is a complete implementation of the NIST SHA-3 cryptographic
hash function, known originally as Keccak.  It gives Perl programmers a
convenient way to calculate SHA3-224, SHA3-256, SHA3-384, and SHA3-512
message digests, as well as variable-length hashes using SHAKE128
and SHAKE256.  The module can handle all types of input, including
partial-byte data.

%package bin
Summary: bin components for the perl-Digest-SHA3 package.
Group: Binaries

%description bin
bin components for the perl-Digest-SHA3 package.


%package dev
Summary: dev components for the perl-Digest-SHA3 package.
Group: Development
Requires: perl-Digest-SHA3-bin = %{version}-%{release}
Provides: perl-Digest-SHA3-devel = %{version}-%{release}
Requires: perl-Digest-SHA3 = %{version}-%{release}

%description dev
dev components for the perl-Digest-SHA3 package.


%package man
Summary: man components for the perl-Digest-SHA3 package.
Group: Default

%description man
man components for the perl-Digest-SHA3 package.


%package perl
Summary: perl components for the perl-Digest-SHA3 package.
Group: Default
Requires: perl-Digest-SHA3 = %{version}-%{release}

%description perl
perl components for the perl-Digest-SHA3 package.


%prep
%setup -q -n Digest-SHA3-1.05
cd %{_builddir}/Digest-SHA3-1.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sha3sum

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::SHA3.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sha3sum.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
