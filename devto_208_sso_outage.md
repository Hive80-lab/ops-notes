---
title: The SSO Outage Runbook: When Nobody Can Log In (Including You)
published: true
tags: devops, security, sre, smallbusiness
canonical_url: https://hive80-lab.github.io/ops-notes/sso-outage-runbook.html
description: The outage nobody can see — the site is up, the database is fine, and every door is locked because the front door (Google Workspace, Okta, Entra ID) is down. Five checks, one break-glass door, and comms that don't run through the thing that broke.
---

A DNS outage makes you hard to find. A **single sign-on outage makes you impossible to enter** — including for you. The status page is up, the site renders, the database is fine, and every door is locked because the front door (Google Workspace, Okta, Microsoft Entra ID, or whatever issues the tokens) is having a bad day. Worst of all, the people who could fix it are locked out too.

The fix is not heroics at 2am. It is five checks to tell lockout from outage, one local door you built in sunlight, and a comms path that does not run through the thing that is down.

The full template with the worked example lives on the [ops-notes SSO outage runbook](https://hive80-lab.github.io/ops-notes/sso-outage-runbook.html) page. Here's the shape of it.

## First five minutes: is it them or you?

Half of "SSO is down" is not an IdP outage — it is one misconfigured app, one expired signing certificate, or one person whose session died. Five checks before you declare anything:

1. **Reproduce from a second device on a different network.** Phone on mobile data, incognito window, another office. One person failing = their session; everyone failing = the IdP.
2. **Test a second app behind the same IdP.** Both dead = provider. One dead = that app's SAML/OIDC config, and this runbook is not your incident.
3. **Check the IdP's status page *and* your own auth logs.** No successful authentications for fifteen minutes across all apps is a signal your logs confirm before any vendor admits anything. `invalid_signature` errors or a today-dated cert expiry point at *your* side, not theirs.
4. **Check the auth domain itself.** If `login.yourcompany.com` stops resolving, this is a DNS problem wearing an SSO costume — run the DNS outage runbook first.
5. **Decide the path out loud, in one sentence:** "Provider-side — activating break-glass and posting status" or "Our side — last change was X, rolling back X."

## Break-glass: the local door you built in sunlight

When the IdP is down, the only way in is a path that **does not go through the IdP**. That path must exist before the outage — building it during one means building it untested. Four properties of a break-glass that actually works:

- **Local admin accounts on the critical few systems** — production host, payment admin panel, DNS/registrar console — kept in a password manager vault that is *not* SSO-gated. An emergency login stored inside the login system is a joke with a punchline at 3am.
- **Printed 2FA recovery codes, sealed, in two locations.** The most common break-glass failure is a second factor that lives in the same dead IdP. Paper survives a provider outage.
- **A named short list of who may use it** — two or three people, written down.
- **Every use logged and closed the same day:** who, what system, how long, and the ticket that rotates the password after. Drill it quarterly — a ten-minute game where one person proves they can get into production without the IdP is the cheapest insurance you will ever buy.

## What still works when login does not

The outage is smaller than it feels — if you know what survives:

- **Existing sessions usually hold.** Tokens were issued before the outage and verified locally or cached; customers already logged in keep working. Panic-resetting sessions converts a sign-in problem into a full outage.
- **Service accounts and CI keep running** if they use API keys rather than interactive SSO. Check before assuming the whole machine is down.
- **New signups and password resets are the real victims.** That is your blast-radius line for comms: "existing users are unaffected; new sign-ins are paused."
- **Email may be behind the same door.** If your mail lives in Google Workspace or Microsoft 365, the IdP outage took your email too. Your comms fallback — independently hosted status page, personal-domain alias, phone/WhatsApp tree — must not depend on the thing that is down.

## Tell people before they tell you

Nothing turns a 40-minute IdP hiccup into a trust incident faster than silence:

- **Internal, minute 5:** "IdP provider outage suspected; break-glass active for [two named people]; existing sessions unaffected; next update 15:20."
- **Status page, minute 15:** "Sign-in is unavailable for some users. Data is safe. Existing sessions are unaffected." Name what works, not just what is broken.
- **Every promised update, on time**, even when it is "no change yet."

## The mistakes that turn an hour into a day

- **The single IdP dependency with no local door.** If production, DNS, and the password manager itself all federate to one provider, an IdP outage is a full company outage.
- **Break-glass stored inside the dead system.** Recovery codes emailed to the SSO-gated inbox. Store the escape hatch *outside* what it escapes from.
- **The password-reset loop.** Resetting everyone's passwords does nothing while the IdP is down, and after recovery it produces a lockout storm, a support queue, and MFA re-enrollment for people who were never affected. Nobody resets anything during an IdP outage.
- **Fixing the provider.** You cannot fix Okta from your laptop. Your job is the two things you own: the local door and the comms.
- **Skipping the review because "the vendor fixed it."** The post-mortem question is not "why did the IdP fail" — it is "why did *we* have no path in, and how long did it take us to notice."

## The numbers that make it real

An eleven-person agency, Friday 9:12am, Google Workspace authentication partially down. The old way: an hour of everyone trying their own browser, two admins resetting passwords "to see if it helps," the founder locked out of production, first customer-facing word a support ticket at 11:30. Five hours of degraded work, 60+ unnecessary password resets, one churned account.

The rerun: second-network reproduction at 9:14, provider confirmed at 9:19, break-glass opened at 9:21 for the two named people, status page at 9:26, email fallback on the founder's personal-domain alias, password rotated and break-glass closed by 9:40. **Total: 34 minutes of lockout for two break-glass users, zero for everyone else, zero password resets.**

The metrics worth tracking: quarterly break-glass drill with a recorded pass rate; time from "confirmed provider-side" to status posted under 15 minutes; **zero** password resets during IdP outages; 100% of critical systems with a documented, recently-tested local-login path.

---

Need this as a fillable template? The free [First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) checklist covers the first half-hour of any incident, the [Ops Starter Kit ($14)](https://hive80lab.gumroad.com/l/ops-starter-kit) is full incident response for small teams, [Vol. 2 ($27)](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) adds advanced incident comms, and the [Ops Mega Bundle ($49)](https://hive80lab.gumroad.com/l/ops-mega-bundle) collects all five kits in one download.