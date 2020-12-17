srpm:
	dnf install -y desktop-file-utils fdupes libappstream-glib python3-devel python3-gobject python3-setuptools python3-wheel
	rpmbuild lutris-unstable.spec --bs --define "_rpmdir $(outdir)"
	return 0
