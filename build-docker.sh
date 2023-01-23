#!/bin/bash
sudo docker build -t mb2hub-frontend ./website/frontend
sudo docker build -t mb2hub-backend ./website/backend
sudo docker compose -f ./website/docker-compose.yml -p mb2hub up
