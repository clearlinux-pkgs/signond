#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : signond
Version  : 8.61
Release  : 7
URL      : https://gitlab.com/accounts-sso/signond/-/archive/VERSION_8.61/signond-VERSION_8.61.tar.gz
Source0  : https://gitlab.com/accounts-sso/signond/-/archive/VERSION_8.61/signond-VERSION_8.61.tar.gz
Summary  : SignOn Framework client library development package
Group    : Development/Tools
License  : LGPL-2.1
Requires: signond-bin = %{version}-%{release}
Requires: signond-data = %{version}-%{release}
Requires: signond-lib = %{version}-%{release}
Requires: signond-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : qttools-dev
Patch1: libdir.patch

%description
SignOn daemon
=============
The SignOn daemon is a D-Bus service which performs user authentication on
behalf of its clients. There are currently authentication plugins for OAuth 1.0
and 2.0, SASL, Digest-MD5, and plain username/password combination.

%package bin
Summary: bin components for the signond package.
Group: Binaries
Requires: signond-data = %{version}-%{release}
Requires: signond-license = %{version}-%{release}

%description bin
bin components for the signond package.


%package data
Summary: data components for the signond package.
Group: Data

%description data
data components for the signond package.


%package dev
Summary: dev components for the signond package.
Group: Development
Requires: signond-lib = %{version}-%{release}
Requires: signond-bin = %{version}-%{release}
Requires: signond-data = %{version}-%{release}
Provides: signond-devel = %{version}-%{release}
Requires: signond = %{version}-%{release}

%description dev
dev components for the signond package.


%package doc
Summary: doc components for the signond package.
Group: Documentation

%description doc
doc components for the signond package.


%package lib
Summary: lib components for the signond package.
Group: Libraries
Requires: signond-data = %{version}-%{release}
Requires: signond-license = %{version}-%{release}

%description lib
lib components for the signond package.


%package license
Summary: license components for the signond package.
Group: Default

%description license
license components for the signond package.


%prep
%setup -q -n signond-VERSION_8.61
cd %{_builddir}/signond-VERSION_8.61
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1663011249
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/signond
cp %{_builddir}/signond-VERSION_%{version}/COPYING %{buildroot}/usr/share/package-licenses/signond/4df5d4b947cf4e63e675729dd3f168ba844483c7
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/signond
/usr/bin/signonpluginprocess

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
/usr/share/dbus-1/services/com.nokia.SingleSignOn.Backup.service

%files dev
%defattr(-,root,root,-)
/usr/include/signon-extension/SignOn/AbstractAccessControlManager
/usr/include/signon-extension/SignOn/AbstractCryptoManager
/usr/include/signon-extension/SignOn/AbstractKeyAuthorizer
/usr/include/signon-extension/SignOn/AbstractKeyManager
/usr/include/signon-extension/SignOn/AbstractSecretsStorage
/usr/include/signon-extension/SignOn/Debug
/usr/include/signon-extension/SignOn/ExtensionInterface
/usr/include/signon-extension/SignOn/KeyHandler
/usr/include/signon-extension/SignOn/abstract-access-control-manager.h
/usr/include/signon-extension/SignOn/abstract-crypto-manager.h
/usr/include/signon-extension/SignOn/abstract-key-authorizer.h
/usr/include/signon-extension/SignOn/abstract-key-manager.h
/usr/include/signon-extension/SignOn/abstract-secrets-storage.h
/usr/include/signon-extension/SignOn/debug.h
/usr/include/signon-extension/SignOn/export.h
/usr/include/signon-extension/SignOn/extension-interface.h
/usr/include/signon-extension/SignOn/key-handler.h
/usr/include/signon-plugins/SignOn/AuthPluginInterface
/usr/include/signon-plugins/SignOn/UiSessionData
/usr/include/signon-plugins/SignOn/authpluginif.h
/usr/include/signon-plugins/SignOn/blobiohandler.h
/usr/include/signon-plugins/SignOn/signonplugincommon.h
/usr/include/signon-plugins/SignOn/uisessiondata.h
/usr/include/signon-plugins/SignOn/uisessiondata_priv.h
/usr/include/signon-plugins/exampledata.h
/usr/include/signon-plugins/exampleplugin.h
/usr/include/signon-plugins/passwordplugin.h
/usr/include/signon-plugins/ssotest2data.h
/usr/include/signon-plugins/ssotest2plugin.h
/usr/include/signon-plugins/ssotestplugin.h
/usr/include/signon-qt5/SignOn/AuthService
/usr/include/signon-qt5/SignOn/AuthSession
/usr/include/signon-qt5/SignOn/Error
/usr/include/signon-qt5/SignOn/Identity
/usr/include/signon-qt5/SignOn/IdentityInfo
/usr/include/signon-qt5/SignOn/SecurityContext
/usr/include/signon-qt5/SignOn/SessionData
/usr/include/signon-qt5/SignOn/authservice.h
/usr/include/signon-qt5/SignOn/authsession.h
/usr/include/signon-qt5/SignOn/identity.h
/usr/include/signon-qt5/SignOn/identityinfo.h
/usr/include/signon-qt5/SignOn/libsignoncommon.h
/usr/include/signon-qt5/SignOn/securitycontext.h
/usr/include/signon-qt5/SignOn/sessiondata.h
/usr/include/signon-qt5/SignOn/signon.h
/usr/include/signon-qt5/SignOn/signonerror.h
/usr/include/signond/accesscontrolmanagerhelper.h
/usr/include/signond/credentialsaccessmanager.h
/usr/include/signond/credentialsdb.h
/usr/include/signond/credentialsdb_p.h
/usr/include/signond/default-crypto-manager.h
/usr/include/signond/default-key-authorizer.h
/usr/include/signond/default-secrets-storage.h
/usr/include/signond/error.h
/usr/include/signond/peercontext.h
/usr/include/signond/pluginproxy.h
/usr/include/signond/signonauthsession.h
/usr/include/signond/signonauthsessionadaptor.h
/usr/include/signond/signoncommon.h
/usr/include/signond/signond-common.h
/usr/include/signond/signondaemon.h
/usr/include/signond/signondaemonadaptor.h
/usr/include/signond/signondisposable.h
/usr/include/signond/signonidentity.h
/usr/include/signond/signonidentityadaptor.h
/usr/include/signond/signonidentityinfo.h
/usr/include/signond/signonsecuritycontext.h
/usr/include/signond/signonsessioncore.h
/usr/include/signond/signonsessioncoretools.h
/usr/include/signond/signontrace.h
/usr/include/signond/signonui_interface.h
/usr/lib64/cmake/SignOnQt5/SignOnQt5Config.cmake
/usr/lib64/cmake/SignOnQt5/SignOnQt5ConfigVersion.cmake
/usr/lib64/libsignon-extension.so
/usr/lib64/libsignon-plugins-common.so
/usr/lib64/libsignon-plugins.so
/usr/lib64/libsignon-qt5.so
/usr/lib64/pkgconfig/SignOnExtension.pc
/usr/lib64/pkgconfig/libsignon-qt5.pc
/usr/lib64/pkgconfig/signon-plugins-common.pc
/usr/lib64/pkgconfig/signon-plugins.pc
/usr/lib64/pkgconfig/signond.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libsignon-qt/html/annotated.html
/usr/share/doc/libsignon-qt/html/annotated_dup.js
/usr/share/doc/libsignon-qt/html/async-dbus-proxy_8cpp_source.html
/usr/share/doc/libsignon-qt/html/async-dbus-proxy_8h_source.html
/usr/share/doc/libsignon-qt/html/authservice_8cpp_source.html
/usr/share/doc/libsignon-qt/html/authservice_8h_source.html
/usr/share/doc/libsignon-qt/html/authsession_8cpp_source.html
/usr/share/doc/libsignon-qt/html/authsession_8h_source.html
/usr/share/doc/libsignon-qt/html/bc_s.png
/usr/share/doc/libsignon-qt/html/bc_sd.png
/usr/share/doc/libsignon-qt/html/bdwn.png
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService_1_1IdentityRegExp-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService_1_1IdentityRegExp.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService_1_1IdentityRegExp.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthService__inherit__graph.dot
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthSession-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthSession.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthSession.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1AuthSession__inherit__graph.dot
/usr/share/doc/libsignon-qt/html/classSignOn_1_1ConnectionManager-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1ConnectionManager.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1ConnectionManager__inherit__graph.dot
/usr/share/doc/libsignon-qt/html/classSignOn_1_1DBusInterface-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1DBusInterface.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1DBusInterface__inherit__graph.dot
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Error-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Error.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Error.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Identity-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Identity.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Identity.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1IdentityInfo-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1IdentityInfo.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1IdentityInfo.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1Identity__inherit__graph.dot
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SecurityContext-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SecurityContext.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SecurityContext.js
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SessionData-members.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SessionData.html
/usr/share/doc/libsignon-qt/html/classSignOn_1_1SessionData.js
/usr/share/doc/libsignon-qt/html/classes.html
/usr/share/doc/libsignon-qt/html/closed.png
/usr/share/doc/libsignon-qt/html/connection-manager_8cpp_source.html
/usr/share/doc/libsignon-qt/html/connection-manager_8h_source.html
/usr/share/doc/libsignon-qt/html/dbusinterface_8cpp_source.html
/usr/share/doc/libsignon-qt/html/dbusinterface_8h_source.html
/usr/share/doc/libsignon-qt/html/debug_8cpp_source.html
/usr/share/doc/libsignon-qt/html/debug_8h_source.html
/usr/share/doc/libsignon-qt/html/deprecated.html
/usr/share/doc/libsignon-qt/html/dir_61c9e5842729cb34568d93cb98ad85b9.html
/usr/share/doc/libsignon-qt/html/dir_61c9e5842729cb34568d93cb98ad85b9_dep.dot
/usr/share/doc/libsignon-qt/html/dir_e68e8157741866f444e17edd764ebbae.html
/usr/share/doc/libsignon-qt/html/doc.png
/usr/share/doc/libsignon-qt/html/docd.png
/usr/share/doc/libsignon-qt/html/doxygen.css
/usr/share/doc/libsignon-qt/html/doxygen.svg
/usr/share/doc/libsignon-qt/html/dynsections.js
/usr/share/doc/libsignon-qt/html/files.html
/usr/share/doc/libsignon-qt/html/files_dup.js
/usr/share/doc/libsignon-qt/html/folderclosed.png
/usr/share/doc/libsignon-qt/html/folderopen.png
/usr/share/doc/libsignon-qt/html/functions.html
/usr/share/doc/libsignon-qt/html/functions_enum.html
/usr/share/doc/libsignon-qt/html/functions_eval.html
/usr/share/doc/libsignon-qt/html/functions_func.html
/usr/share/doc/libsignon-qt/html/functions_type.html
/usr/share/doc/libsignon-qt/html/functions_vars.html
/usr/share/doc/libsignon-qt/html/graph_legend.dot
/usr/share/doc/libsignon-qt/html/graph_legend.html
/usr/share/doc/libsignon-qt/html/hierarchy.html
/usr/share/doc/libsignon-qt/html/hierarchy.js
/usr/share/doc/libsignon-qt/html/identity_8cpp_source.html
/usr/share/doc/libsignon-qt/html/identity_8h_source.html
/usr/share/doc/libsignon-qt/html/identityinfo_8cpp_source.html
/usr/share/doc/libsignon-qt/html/identityinfo_8h_source.html
/usr/share/doc/libsignon-qt/html/index.html
/usr/share/doc/libsignon-qt/html/index.qhp
/usr/share/doc/libsignon-qt/html/inherit_graph_0.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_1.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_2.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_3.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_4.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_5.dot
/usr/share/doc/libsignon-qt/html/inherit_graph_6.dot
/usr/share/doc/libsignon-qt/html/inherits.html
/usr/share/doc/libsignon-qt/html/jquery.js
/usr/share/doc/libsignon-qt/html/libsignoncommon_8h_source.html
/usr/share/doc/libsignon-qt/html/menu.js
/usr/share/doc/libsignon-qt/html/menudata.js
/usr/share/doc/libsignon-qt/html/namespaceSignOn.html
/usr/share/doc/libsignon-qt/html/namespaceSignOnTests.html
/usr/share/doc/libsignon-qt/html/namespacemembers.html
/usr/share/doc/libsignon-qt/html/namespacemembers_enum.html
/usr/share/doc/libsignon-qt/html/namespacemembers_eval.html
/usr/share/doc/libsignon-qt/html/namespacemembers_type.html
/usr/share/doc/libsignon-qt/html/nav_f.png
/usr/share/doc/libsignon-qt/html/nav_fd.png
/usr/share/doc/libsignon-qt/html/nav_g.png
/usr/share/doc/libsignon-qt/html/nav_h.png
/usr/share/doc/libsignon-qt/html/nav_hd.png
/usr/share/doc/libsignon-qt/html/navtree.css
/usr/share/doc/libsignon-qt/html/navtree.js
/usr/share/doc/libsignon-qt/html/navtreedata.js
/usr/share/doc/libsignon-qt/html/navtreeindex0.js
/usr/share/doc/libsignon-qt/html/navtreeindex1.js
/usr/share/doc/libsignon-qt/html/open.png
/usr/share/doc/libsignon-qt/html/pages.html
/usr/share/doc/libsignon-qt/html/resize.js
/usr/share/doc/libsignon-qt/html/securitycontext_8cpp_source.html
/usr/share/doc/libsignon-qt/html/securitycontext_8h_source.html
/usr/share/doc/libsignon-qt/html/securitycontextpriv_8h_source.html
/usr/share/doc/libsignon-qt/html/sessiondata_8h_source.html
/usr/share/doc/libsignon-qt/html/signon_8h_source.html
/usr/share/doc/libsignon-qt/html/signonerror_8h_source.html
/usr/share/doc/libsignon-qt/html/splitbar.png
/usr/share/doc/libsignon-qt/html/splitbard.png
/usr/share/doc/libsignon-qt/html/sync_off.png
/usr/share/doc/libsignon-qt/html/sync_on.png
/usr/share/doc/libsignon-qt/html/tab_a.png
/usr/share/doc/libsignon-qt/html/tab_ad.png
/usr/share/doc/libsignon-qt/html/tab_b.png
/usr/share/doc/libsignon-qt/html/tab_bd.png
/usr/share/doc/libsignon-qt/html/tab_h.png
/usr/share/doc/libsignon-qt/html/tab_hd.png
/usr/share/doc/libsignon-qt/html/tab_s.png
/usr/share/doc/libsignon-qt/html/tab_sd.png
/usr/share/doc/libsignon-qt/html/tabs.css
/usr/share/doc/libsignon-qt/html/todo.html
/usr/share/doc/libsignon-qt/qch/signon.qch
/usr/share/doc/signon-plugins-dev/example/exampledata.h
/usr/share/doc/signon-plugins-dev/example/exampleplugin.cpp
/usr/share/doc/signon-plugins-dev/example/exampleplugin.h
/usr/share/doc/signon-plugins-dev/example/exampleplugin.pro
/usr/share/doc/signon-plugins/html/annotated.html
/usr/share/doc/signon-plugins/html/annotated_dup.js
/usr/share/doc/signon-plugins/html/authpluginif_8h_source.html
/usr/share/doc/signon-plugins/html/bc_s.png
/usr/share/doc/signon-plugins/html/bc_sd.png
/usr/share/doc/signon-plugins/html/bdwn.png
/usr/share/doc/signon-plugins/html/blobiohandler_8cpp_source.html
/usr/share/doc/signon-plugins/html/blobiohandler_8h_source.html
/usr/share/doc/signon-plugins/html/classAuthPluginInterface-members.html
/usr/share/doc/signon-plugins/html/classAuthPluginInterface.html
/usr/share/doc/signon-plugins/html/classAuthPluginInterface.js
/usr/share/doc/signon-plugins/html/classAuthPluginInterface_1_1Interface.html
/usr/share/doc/signon-plugins/html/classAuthPluginInterface__inherit__graph.dot
/usr/share/doc/signon-plugins/html/classSignOn_1_1BlobIOHandler-members.html
/usr/share/doc/signon-plugins/html/classSignOn_1_1BlobIOHandler.html
/usr/share/doc/signon-plugins/html/classSignOn_1_1BlobIOHandler__inherit__graph.dot
/usr/share/doc/signon-plugins/html/classSignOn_1_1UiSessionData-members.html
/usr/share/doc/signon-plugins/html/classSignOn_1_1UiSessionData.html
/usr/share/doc/signon-plugins/html/classSignOn_1_1UiSessionData.js
/usr/share/doc/signon-plugins/html/classSignOn_1_1UiSessionData__inherit__graph.dot
/usr/share/doc/signon-plugins/html/classes.html
/usr/share/doc/signon-plugins/html/closed.png
/usr/share/doc/signon-plugins/html/dir_255383846029633073d68bbe3f80a8e9.html
/usr/share/doc/signon-plugins/html/dir_255383846029633073d68bbe3f80a8e9.js
/usr/share/doc/signon-plugins/html/dir_61c9e5842729cb34568d93cb98ad85b9.html
/usr/share/doc/signon-plugins/html/dir_61c9e5842729cb34568d93cb98ad85b9_dep.dot
/usr/share/doc/signon-plugins/html/dir_af34ae28ea23134a8ded716ce53b273a.html
/usr/share/doc/signon-plugins/html/dir_af34ae28ea23134a8ded716ce53b273a.js
/usr/share/doc/signon-plugins/html/dir_d823c49a50e17c23ae924694bd3125c3.html
/usr/share/doc/signon-plugins/html/dir_d823c49a50e17c23ae924694bd3125c3.js
/usr/share/doc/signon-plugins/html/dir_d823c49a50e17c23ae924694bd3125c3_dep.dot
/usr/share/doc/signon-plugins/html/dir_e68e8157741866f444e17edd764ebbae.html
/usr/share/doc/signon-plugins/html/doc.png
/usr/share/doc/signon-plugins/html/docd.png
/usr/share/doc/signon-plugins/html/doxygen.css
/usr/share/doc/signon-plugins/html/doxygen.svg
/usr/share/doc/signon-plugins/html/dynsections.js
/usr/share/doc/signon-plugins/html/files.html
/usr/share/doc/signon-plugins/html/files_dup.js
/usr/share/doc/signon-plugins/html/folderclosed.png
/usr/share/doc/signon-plugins/html/folderopen.png
/usr/share/doc/signon-plugins/html/functions.html
/usr/share/doc/signon-plugins/html/functions_func.html
/usr/share/doc/signon-plugins/html/graph_legend.dot
/usr/share/doc/signon-plugins/html/graph_legend.html
/usr/share/doc/signon-plugins/html/hierarchy.html
/usr/share/doc/signon-plugins/html/hierarchy.js
/usr/share/doc/signon-plugins/html/index.html
/usr/share/doc/signon-plugins/html/index.qhp
/usr/share/doc/signon-plugins/html/inherit_graph_0.dot
/usr/share/doc/signon-plugins/html/inherit_graph_1.dot
/usr/share/doc/signon-plugins/html/inherit_graph_2.dot
/usr/share/doc/signon-plugins/html/inherits.html
/usr/share/doc/signon-plugins/html/ipc_8h_source.html
/usr/share/doc/signon-plugins/html/jquery.js
/usr/share/doc/signon-plugins/html/menu.js
/usr/share/doc/signon-plugins/html/menudata.js
/usr/share/doc/signon-plugins/html/namespaceSignOn.html
/usr/share/doc/signon-plugins/html/namespacemembers.html
/usr/share/doc/signon-plugins/html/namespacemembers_enum.html
/usr/share/doc/signon-plugins/html/namespacemembers_eval.html
/usr/share/doc/signon-plugins/html/nav_f.png
/usr/share/doc/signon-plugins/html/nav_fd.png
/usr/share/doc/signon-plugins/html/nav_g.png
/usr/share/doc/signon-plugins/html/nav_h.png
/usr/share/doc/signon-plugins/html/nav_hd.png
/usr/share/doc/signon-plugins/html/navtree.css
/usr/share/doc/signon-plugins/html/navtree.js
/usr/share/doc/signon-plugins/html/navtreedata.js
/usr/share/doc/signon-plugins/html/navtreeindex0.js
/usr/share/doc/signon-plugins/html/open.png
/usr/share/doc/signon-plugins/html/resize.js
/usr/share/doc/signon-plugins/html/signonplugincommon_8h_source.html
/usr/share/doc/signon-plugins/html/splitbar.png
/usr/share/doc/signon-plugins/html/splitbard.png
/usr/share/doc/signon-plugins/html/sync_off.png
/usr/share/doc/signon-plugins/html/sync_on.png
/usr/share/doc/signon-plugins/html/tab_a.png
/usr/share/doc/signon-plugins/html/tab_ad.png
/usr/share/doc/signon-plugins/html/tab_b.png
/usr/share/doc/signon-plugins/html/tab_bd.png
/usr/share/doc/signon-plugins/html/tab_h.png
/usr/share/doc/signon-plugins/html/tab_hd.png
/usr/share/doc/signon-plugins/html/tab_s.png
/usr/share/doc/signon-plugins/html/tab_sd.png
/usr/share/doc/signon-plugins/html/tabs.css
/usr/share/doc/signon-plugins/html/uisessiondata_8h_source.html
/usr/share/doc/signon-plugins/html/uisessiondata__priv_8h_source.html
/usr/share/doc/signon-plugins/qch/signon.qch
/usr/share/doc/signon/html/bc_s.png
/usr/share/doc/signon/html/bc_sd.png
/usr/share/doc/signon/html/bdwn.png
/usr/share/doc/signon/html/closed.png
/usr/share/doc/signon/html/dir_61c9e5842729cb34568d93cb98ad85b9.html
/usr/share/doc/signon/html/dir_61c9e5842729cb34568d93cb98ad85b9_dep.dot
/usr/share/doc/signon/html/dir_e68e8157741866f444e17edd764ebbae.html
/usr/share/doc/signon/html/doc.png
/usr/share/doc/signon/html/docd.png
/usr/share/doc/signon/html/doxygen.css
/usr/share/doc/signon/html/doxygen.svg
/usr/share/doc/signon/html/dynsections.js
/usr/share/doc/signon/html/folderclosed.png
/usr/share/doc/signon/html/folderopen.png
/usr/share/doc/signon/html/graph_legend.dot
/usr/share/doc/signon/html/graph_legend.html
/usr/share/doc/signon/html/index.html
/usr/share/doc/signon/html/index.qhp
/usr/share/doc/signon/html/jquery.js
/usr/share/doc/signon/html/menu.js
/usr/share/doc/signon/html/menudata.js
/usr/share/doc/signon/html/nav_f.png
/usr/share/doc/signon/html/nav_fd.png
/usr/share/doc/signon/html/nav_g.png
/usr/share/doc/signon/html/nav_h.png
/usr/share/doc/signon/html/nav_hd.png
/usr/share/doc/signon/html/navtree.css
/usr/share/doc/signon/html/navtree.js
/usr/share/doc/signon/html/navtreedata.js
/usr/share/doc/signon/html/navtreeindex0.js
/usr/share/doc/signon/html/open.png
/usr/share/doc/signon/html/resize.js
/usr/share/doc/signon/html/splitbar.png
/usr/share/doc/signon/html/splitbard.png
/usr/share/doc/signon/html/sync_off.png
/usr/share/doc/signon/html/sync_on.png
/usr/share/doc/signon/html/tab_a.png
/usr/share/doc/signon/html/tab_ad.png
/usr/share/doc/signon/html/tab_b.png
/usr/share/doc/signon/html/tab_bd.png
/usr/share/doc/signon/html/tab_h.png
/usr/share/doc/signon/html/tab_hd.png
/usr/share/doc/signon/html/tab_s.png
/usr/share/doc/signon/html/tab_sd.png
/usr/share/doc/signon/html/tabs.css
/usr/share/doc/signon/qch/signon.qch

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsignon-extension.so.1
/usr/lib64/libsignon-extension.so.1.0
/usr/lib64/libsignon-extension.so.1.0.0
/usr/lib64/libsignon-plugins-common.so.1
/usr/lib64/libsignon-plugins-common.so.1.0
/usr/lib64/libsignon-plugins-common.so.1.0.0
/usr/lib64/libsignon-plugins.so.1
/usr/lib64/libsignon-plugins.so.1.0
/usr/lib64/libsignon-plugins.so.1.0.0
/usr/lib64/libsignon-qt5.so.1
/usr/lib64/libsignon-qt5.so.1.0
/usr/lib64/libsignon-qt5.so.1.0.0
/usr/lib64/signon/libexampleplugin.so
/usr/lib64/signon/libpasswordplugin.so
/usr/lib64/signon/libssotest2plugin.so
/usr/lib64/signon/libssotestplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/signond/4df5d4b947cf4e63e675729dd3f168ba844483c7
