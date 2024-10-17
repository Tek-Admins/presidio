docker build ./presidio-anonymizer -t presidio/presidio-anonymizer

docker build ./presidio-analyzer -t bobwashere758/presidio-analyzer:2.2.356

docker tag presidio-analyzer2.2.359:latest bobwashere758/presidio-analyzer:2.2.359
docker push bobwashere758/presidio-analyzer:2.2.359


docker tag presidio-anonymizer2.2.359:latest bobwashere758/presidio-anonymizer:2.2.359
docker push bobwashere758/presidio-anonymizer:2.2.359


docker tag presidio-image-redactor2.2.359:latest bobwashere758/presidio-image-redactor:2.2.359
docker push bobwashere758/presidio-image-redactor:2.2.359

