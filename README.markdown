Static website for the LSM 2013

```bash
virtualenv -p /usr/bin/python2.7 rmll-website
cd rmll-website/
source bin/activate
pip install -r requirements.txt
git clone git://github.com/RMLL/rmll2013-website.git
cd rmll2013-website/
fab serve
deactivate
```

