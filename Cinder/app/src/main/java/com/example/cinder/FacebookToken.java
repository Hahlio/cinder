package com.example.cinder;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class FacebookToken {
    @SerializedName("token")
    @Expose
    private String token;

    @SerializedName("deviceid")
    @Expose
    private String deviceid;

    public String gettoken() {
        return token;
    }

    public void settoken(String token) {
        this.token = token;
    }

    public String getDeviceid() {
        return deviceid;
    }

    public void setDeviceid(String deviceid) {
        this.deviceid = deviceid;
    }
}
