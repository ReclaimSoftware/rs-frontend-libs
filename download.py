import json
from subprocess import check_call


def main():
    with open('libraries.json', 'rb') as f:
        info = json.loads(unicode(f.read(), 'utf-8'))
    for library in info['libraries']:
        for version in library['versions']:
            for file in library['files']:
                download_file_version(library, file, version)
    print 'Done.'


def download_file_version(library, file, version):

    parts = file.split('/')
    filename = parts[-1]
    if len(parts) > 1:
        filedir = '/' + '/'.join(parts[:-1])
    else:
        filedir = ""

    dest_dir = "public/libs/%s/%s%s" % (library['slug'], version, filedir)
    dest_path = "%s/%s" % (dest_dir, filename)
    url = library['url'] % (version, file)

    print
    print url
    check_call(['mkdir', '-p', dest_dir])
    check_call(['bash', '-c', "curl --silent '%s' > '%s'" % (url, dest_path)])


if __name__ == '__main__':
  main()
