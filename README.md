# projet-fil-rouge-iaas

###### Déploiement de serverless 
   Etapes de la mise en place de serverless dans Serverless_deployment_log.txt


###### Portage de l'installation avec venv : 

   $ git clone https://github.com/djangit/projet-fil-rouge-iaas.git
   $ cd projet-fil-rouge-iaas/
   $ . ./venv/bin/activate
   (venv) $ sls deploy

###### Utilisation : exemple de requête 
   curl -X POST "https://27gckgi4wk.execute-api.eu-west-1.amazonaws.com/dev/toto" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@coverage.jpg;type=image/jpg"

###### Résultat attendu : 
   un json composé de 2 parties : le contenu du fichier, les métadonnées (nom du fichier, taille, mimetype)


