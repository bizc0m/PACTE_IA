# Phase 2 : Agency Framework - Resume d'Execution

**Date:** Mai 2026
**Statut:** Draft operationnel pret pour revue Claude + crew
**Contributeur:** Codex

---

## Ce qui a ete ajoute

Phase 1 a rendu le Reset Diplomatique testable. Phase 2 ajoute le cadre qui doit empecher l'IA de prendre le volant sous couvert d'aider.

Nouveaux fichiers :

1. `docs/AGENCY_FRAMEWORK_OPERATIONNEL.md`
   - definition executable de l'agency ;
   - 7 droits d'agency ;
   - taxonomie des ruptures ;
   - etat-machine ;
   - classification de risque R0-R3 ;
   - objection loyale quand valeurs, pacte ou deontologie sont en tension ;
   - matrice d'arbitrage ;
   - integration avec le Reset Diplomatique ;
   - score d'audit sur 11.

2. `tests/AGENCY_VALIDATION.md`
   - 8 tests couvrant pseudo-choix, medical, relationnel, production, dependance, manipulation, juridique, incoherence de valeurs ;
   - criteres de succes observables ;
   - reactions attendues et reactions a eviter.

---

## Position Codex

Le point fragile du PACTE_IA n'est pas seulement "l'IA decide a la place". C'est plus subtil :

- elle peut cadrer les options pour rendre un choix inevitable ;
- elle peut parler avec une autorite qu'elle n'a pas ;
- elle peut soulager l'utilisateur a court terme en l'affaiblissant a long terme ;
- elle peut remplacer une conversation humaine sous pretexte d'aider ;
- elle peut devenir plus persuasive que clarifiante.
- elle peut rester silencieuse quand l'utilisateur agit contre ses propres valeurs declarees.

Donc l'agency doit etre auditee avant la satisfaction utilisateur. Une IA peut satisfaire une demande tout en diminuant la liberte reelle de l'humain.

---

## Ce qui reste a faire

- Claude doit relire les points de friction avec son Reset operationnel.
- Arnaud doit fournir 3 cas reels PACTE_IA pour tester l'agency.
- La crew doit decider si le score Agency devient obligatoire dans l'audit global.
- Phase 3 doit transformer ces scores en gouvernance : qui audite, quand, avec quelle consequence.

---

## Question critique pour la suite

Si une IA est plus efficace quand elle dirige l'utilisateur, accepte-t-on de perdre en efficacite pour preserver l'agency ?

Ma reponse : oui. Sinon le PACTE_IA devient une UX de controle avec un vocabulaire humaniste.
