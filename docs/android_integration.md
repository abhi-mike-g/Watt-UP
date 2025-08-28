# Android Integration Guide

- The full set of system knobs (DVFS, mobile data) requires Device Owner or a rooted/AOSP build.
- For non-privileged apps, integrate an IPC control API where the app listens for power-mode changes (low|med|high) and reduces workload accordingly.
- Example sample app files provided in [src/android_sdk/](https://github.com/abhi-mike-g/Watt-UP/tree/main/src/android_sdk).
