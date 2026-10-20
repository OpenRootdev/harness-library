# Listed in Harness Library : mise en avant communautaire gratuite de 14 jours

Le programme récompense les contributeurs qui facilitent la découverte de harnesses réutilisables. Il n'y a ni paiement ni obligation d'utiliser Harneloop.

1. Faites approuver votre fiche.
2. Copiez l'extrait du badge depuis sa page détaillée dans l'annuaire et placez-le dans les **30 premières lignes** du README de la branche par défaut du dépôt source.
3. Conservez le lien de l'image vers votre fiche exacte. La prochaine vérification accorde une seule **période de 14 jours**, à compter du premier contrôle réussi en UTC.

Exemple :

```md
[![Listed in Harness Library](https://openrootdev.github.io/harness-library/badges/your-slug.svg)](https://openrootdev.github.io/harness-library/harnesses/your-slug/)
```

Le Markdown exact ou une image HTML liée équivalente sont acceptés. Le texte alternatif de l'image doit être « Listed in Harness Library ». Les exemples dans des blocs de code ou des commentaires HTML ne sont pas admissibles.

Les anciens liens retour `https://openrootdev.github.io/harness-library/#your-slug` restent admissibles et mènent à la page correspondante. Utilisez l'URL réelle de la page pour les nouveaux badges.

Les fiches actives apparaissent avant les fiches ordinaires, puis par ordre alphabétique dans chaque groupe. Les filtres de recherche et de catégorie s'appliquent toujours. L'annuaire affiche un label **Community boost** et son expiration sur la page détaillée. Il s'agit d'un placement promotionnel ; le statut de l'examen et les affirmations de qualité restent indépendants.

Le workflow quotidien sur la branche main de confiance ne lit que les métadonnées publiques des README GitHub. Il enregistre l'attribution initiale, l'expiration, la dernière présence du badge et l'heure du contrôle dans `data/boosts.json`. Il n'exécute pas de code provenant d'un dépôt de harness. Retirer le badge interrompt la mise en avant après le prochain contrôle. Le remettre ne peut rétablir que le temps restant de la période initiale. Les attributions expirées ne se renouvellent jamais automatiquement. Les soumissions en double, changements de slug ou transferts de dépôt ne donnent pas droit à une deuxième récompense initiale pour le même harness ; les mainteneurs vérifient son identité.

Si GitHub est temporairement indisponible, aucune nouvelle mise en avant n'est accordée. Les badges déjà vérifiés restent admissibles pendant au plus 48 heures sans nouveau contrôle, et jamais au-delà de leur expiration initiale. La génération statique et le navigateur revérifient tous deux les horodatages. Les enregistrements nécessitent l'approbation d'un mainteneur ; modifier un champ JSON dans une soumission ne peut pas accorder de mise en avant.

Le badge peut rester après expiration. Toute nouvelle politique serait discutée publiquement ; il n'existe ni promotion récurrente cachée ni classement payant.

Les badges émis avant la migration vers Kaelux Labs à `https://ker102.github.io/harness-library/` restent admissibles. La migration ne relance pas la période initiale de 14 jours. Mettez à jour l'image et le lien retour vers la nouvelle adresse canonique lorsque cela vous convient.
