package com.example.ondeviceagent

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log

class PowerAgentService : Service() {
    override fun onBind(intent: Intent?): IBinder? { return null }
    override fun onCreate() {
        super.onCreate()
        Log.i("PowerAgent","Service created")
    }
}
