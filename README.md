# Wistia Video Downloader

Usage:

```shell
python main.py
[...enter Wistia video details]
[...enter desired name of the video]
```

To get the Wistia Video Details, right click on the video and **Get video details**. It generally looks like this

```html
<p><a href="https://wistia.com?wvideo=5n7lt2ij69"><img src="https://embedwistia-a.akamaihd.net/deliveries/48f1d62d1ceddb4284ad9cf67c916235.jpg?image_play_button_size=2x&amp;image_crop_resized=960x540&amp;image_play_button=1&amp;image_play_button_color=fa4fa0e0" style="width: 400px; height: 225px;" width="400" height="225"></a></p><p><a href="https://wistia.com?wvideo=5n7lt2ij69">The video hosting platform made for B2B marketers | Wistia</a></p>
```

## Requirements

- threading
- requests