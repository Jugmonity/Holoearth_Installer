import urllib.request

from tqdm import tqdm

link = "https://cdn.holoearth.com/0.12.0-f69e8695-b348-484a-9e7a-102bd1cda658/0.12.0/windows/build/f69e8695-b348-484a-9e7a-102bd1cda658/Holoearth.zip"
class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

if __name__ == "__main__":
    download_url(link, "Holoearth.zip")