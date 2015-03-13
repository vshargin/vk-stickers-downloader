Bulk Image Downloader
======================

aka VK Sticker Grabber

## Usage

```yaml
# Either just specify URLs to grab, like this:
otto:
  - https://vk.com/images/stickers/346/512.png
  - https://vk.com/images/stickers/347/512.png
  - https://vk.com/images/stickers/348/512.png
  - ...

# ...or use the `range' shorthand:
foxy: {range: [233, 264]}
```

```
$ python3 grab.py config.yml
$ ls
foxy    otto    config.yml
$ ls foxy
1.png   2.png   ...
```

## webpify.bat
Usage: `webpify.bat [/path/to/cwebp]`

Use `webpify.bat` to convert downloaded stickers from PNG to WebP. You can use WebP images as stickers in Telegram. You'll also need `cwebp`, which you can get [here](http://downloads.webmproject.org/releases/webp/index.html).