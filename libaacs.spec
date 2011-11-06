%global tarball_date 20111105
%global git_hash 876f45a3f727eb6f06cdb2b0128f857226346e59
%global git_short %(echo '%{git_hash}' | cut -c -13)

Name:           libaacs
Version:        0.2
Release:        0.3.%{tarball_date}git%{git_short}%{?dist}
Summary:        Open implementation of AACS specification
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libaacs.html
# No release yet. Use the commands below to generate a tarball.
# git clone git://git.videolan.org/libaacs.git
# cd libaacs
# git archive --format=tar %{git_hash} --prefix=libaacs/ | bzip2 > ../libaacs-$( date +%Y%m%d )git%{git_short}.tar.bz2
Source0:        %{name}-%{tarball_date}git%{git_short}.tar.bz2
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  libgcrypt-devel
BuildRequires:  flex
BuildRequires:  bison


%description
This library is an open implementation of the AACS specification.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
sed -i -e 's/\r//' KEYDB.cfg


%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING KEYDB.cfg README.txt
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libaacs.pc


%changelog
* Sat Nov 05 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.3.20111105git876f45a3f727e
- Update to latest snapshot.

* Tue Sep 27 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.2.20110925gite854d6673ad6c
- Make the devel package require arch-specific base package.

* Sun Sep 25 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.1.20110925gite854d6673ad6c
- Update to latest snapshot.

* Sun Jul 10 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.6.20110710git964342fbf3ed6
- Update to latest snapshot.

* Sun May 15 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.5.20110515git497c22423d0e7
- Update to latest snapshot.

* Fri Jan 07 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.4.20110107gite7aa4fd42c0d4
- Update to latest snapshot.

* Sun Nov 14 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.3.20101114gitfb77542a8f6c7
- Update to latest snapshot.

* Thu Oct 21 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.2.20101021git00b2df2bb7598
- Fix release tag.
- Update to latest snapshot.

* Tue Aug 17 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.1.20100817
- Initial Fedora release.