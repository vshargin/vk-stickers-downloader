import os
import sys
from urllib2 import urlopen, HTTPError, URLError


def dlfile(url, num):
    # Open the url
    try:
        f = urlopen(url)
        print "Downloading " + url

        # Open our local file for writing
        with open("%03d_%s" % (num, os.path.basename(url)), "wb") as local_file:
            local_file.write(f.read())
    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def main():
    if len(sys.argv) < 3:
        sys.exit("Please specify a download range.")
    try:
        range_lower = int(sys.argv[1])
        range_upper = int(sys.argv[2])
        if range_lower > range_upper:
            raise ValueError
    except ValueError:
        sys.exit("Have you specified a valid range? Seems like nope.")

    download_range = range(range_lower, range_upper + 1)

    base_url = "https://vk.com/images/stickers/"
    resolution = "/512.png"

    for i in download_range:
        url = base_url + str(i) + resolution
        dlfile(url, i)

if __name__ == "__main__":
    main()
