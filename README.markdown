Static website for the LSM 2013

```bash
virtualenv -p /usr/bin/python2.7 rmll-website
cd rmll-website/
source bin/activate
git clone git://github.com/RMLL/rmll2013-website.git
cd rmll2013-website/
pip install -r requirements.txt
fab serve
deactivate
```

