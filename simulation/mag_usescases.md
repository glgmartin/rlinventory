# MessageAggregator uses cases

## le MAG reçoit une séquence

La séquence est nouvelle (on ne peut lui envoyer aucune ancienne séquence)

Le MAG stocke la séquence en mémoire

Le MAG vérifie ce qui est faisable dans la séquence

Le MAG envoie tous les messages faisables de la séquence dans la file d'événements

## le MAG reçoit un msg

Le MAG cherche s'il connait l'événement

### L'événement est connu

Il a été redirigé par un MsgHandler parce qu'il appartient à une séquence

#### L'état de l'événement est != de FINISHED

Erreur

#### L'état est FINISHED

Il faut trouver à quelle séquence appartient le message reçu

Il faut demander à la séquence de se mettre a jour

Il faut demander à la séquence d'envoyer les nouveaux messages disponibles

Si la séquence est finie, elle doit nous le dire

##### Si la séquence est finie

On la supprime elle et tous ses messages en mémoire

### L'événement est inconnu

#### L'état est != PENDING 

Erreur

#### L'état est PENDING

L'événement doit être routé vers le bon handler à travers la file d'événements

On marque l'état de l'événement à READY
