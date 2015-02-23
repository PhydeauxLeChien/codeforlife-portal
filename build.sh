#!/bin/bash
pip install -r /opt/codeforlife-deploy/requirements.txt
pip install https://bitbucket.org/rptlab/reportlab/get/tip.zip
ssh-agent /opt/codeforlife-deploy/install-portal.sh
ssh-agent /opt/codeforlife-deploy/install-rapid-router.sh
echo "Following packages present:"
pip freeze
echo "--------------------------------------------------------------------------------"
