Name     : c_rehash
Version  : 1
Release  : 9
Source0  : c_rehash.c
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: c_rehash-bin
BuildRequires: openssl-dev

%description
No detailed description available

%package bin
Summary: bin components for the c_rehash package.
Group: Binaries

%description bin
bin components for the c_rehash package.


%prep
mkdir c_rehash-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589405084
gcc $(CFLAGS) %{SOURCE0} -o c_rehash -lssl -lcrypto


%install
export SOURCE_DATE_EPOCH=1589405084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp c_rehash %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/c_rehash
