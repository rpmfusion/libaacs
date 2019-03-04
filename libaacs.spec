#global snapshot 1
%global tarball_date 20111105
%global git_hash 876f45a3f727eb6f06cdb2b0128f857226346e59
%global git_short %(echo '%{git_hash}' | cut -c -13)

Name:           libaacs
Version:        0.9.0
Release:        6%{?snapshot:.%{tarball_date}git%{git_short}}%{?dist}
Summary:        Open implementation of AACS specification
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libaacs.html
%if 0%{?snapshot}
# Use the commands below to generate a tarball.
# git clone git://git.videolan.org/libaacs.git
# cd libaacs
# git archive --format=tar %{git_hash} --prefix=libaacs/ | bzip2 > ../libaacs-$( date +%Y%m%d )git%{git_short}.tar.bz2
Source0:        %{name}-%{tarball_date}git%{git_short}.tar.bz2
%else
Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
%endif

%if 0%{?snapshot}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  flex
BuildRequires:  bison


%description
This library is an open implementation of the AACS specification.


%package utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains test utilities for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%if 0%{?snapshot}
%setup -q -n %{name}
%else
%setup -q
%endif
sed -i -e 's/\r//' KEYDB.cfg


%build
%if 0%{?snapshot}
autoreconf -vif
%endif
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc KEYDB.cfg ChangeLog README.txt
%license COPYING 
%{_libdir}/*.so.*

%files utils
%{_bindir}/aacs_info

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libaacs.pc


%changelog
* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 20 2018 Xavier Bachelot <xavier@bachelot.org> 0.9.0-4
- Add BR: gcc.
- Use %%ldconfig_scriptlets.
- Remove Group:s.

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Xavier Bachelot <xavier@bachelot.org> 0.9.0-1
- Update to 0.9.0.

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 15 2015 Xavier Bachelot <xavier@bachelot.org> 0.8.1-1
- Update to 0.8.1.

* Tue Jan 27 2015 Xavier Bachelot <xavier@bachelot.org> 0.8.0-1
- Update to 0.8.0.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.7.1-1
- Update to 0.7.1.

* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> 0.7.0-4
- Add patch for libgcrypt 1.6 support.
- Tweak the Release: tag to accomodate rpmdev-bumpspec.
- Modernize specfile.

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-3
- Rebuilt for libgcrypt

* Thu Dec 19 2013 Xavier Bachelot <xavier@bachelot.org> 0.7.0-2
- Move test utilities to their own subpackage to avoid potential multilib conflict.

* Thu Dec 19 2013 Xavier Bachelot <xavier@bachelot.org> 0.7.0-1
- Update to 0.7.0.

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-4
- Rebuilt

* Sun Sep 08 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-3
- Better rpath fix.

* Wed Aug 21 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-2
- Fix rpath issue with aacs_info.

* Mon Mar 04 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-1
- Update to 0.6.0.
- Switch back to bison.

* Mon Sep 03 2012 Xavier Bachelot <xavier@bachelot.org> 0.5.0-1
- Update to 0.5.0.
- Use byacc instead of bison, libaacs doesn't build with bison 2.6.1.

* Mon May 07 2012 Xavier Bachelot <xavier@bachelot.org> 0.4.0-1
- Update to 0.4.0.

* Thu Mar 22 2012 Xavier Bachelot <xavier@bachelot.org> 0.3.1-1
- Update to 0.3.1.

* Fri Dec 02 2011 Xavier Bachelot <xavier@bachelot.org> 0.3.0-1
- First official upstream release.

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
