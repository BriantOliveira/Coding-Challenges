/**
 * Implement a cache function
 */

function Cache() {
    let data = {};
    let self = this;

    const now = () => {
        return new Date().getTime()/1000;
    }

    /**
     * Object that will hold the cache value, and expiration time
     * @param {*} expiration - The expiration time
     * @param {*} value - The value for the cache entry
     */
    const CacheEntry = function(expiration, value) {
        this.expiration = expiration;
        this.value = value;
    }

    /**
     * Creates a new cache entry
     * @param {*} value  - The value to set the cache entry
     * @returns {CacheEntry} - the cache entry object
     */
    CacheEntry.create = function(value) {
        return new CacheEntry(now(), value);
    }

    /**
     *  Returns an array of all currently set keys
     */
    this.keys = () => {
        let keys = [];
        for (let key in data) {
            if(data.hasOwnProperty(key)) {
                keys.push(key);
            }
        }
    }

    /**
     * Checks if there is a key currently set on cache
     * @param key - The key entry to check
     *  @returns {boolean} - True if the key is set, false otherwise
     */
    this.has = (key) => {
        return data.hasOwnProperty(key);
    }

    /**
     * Checks if the cache entry is expired
     * @param {*} initialEntryTime - The entry time of the cache entry
     * @param {*} currentTime - the current time
     * @returns { boolean } - true if the cache entry is expired, false otherwise.
     */
    this.expired = (initialEntryTime, currentTime) => {
        if (!currentTime) {
            currentTime = now();
        }
        return initialEntryTime < currentTime;
    }

    /**
     * Gets a cache entry with the given key
     * @param {*} key - the key of the cache entry
     * @returns the cache entry if set or undefined if not set
     */
    this.get = (key) => {
        if(self.has(key)) {
            let entry = data[key];
            if(entry.expiration > now()) {
                return entry.value;
            }
        }
        return undefined;
    }

    /*
    * Sets a cache entry with the given key and value
    * @param {*} key - the key of the cache entry
    * @param {*} defaultValue - the value to set of the cache entry
    */
    this.set = (key, defaultValue) => {
        if(!self.has(key)) {
            data[key] = CacheEntry.create(defaultValue);
        }
    }

    /**
     * Clear all caches
     */
    this.clear = () => {
        for (let key in data) {
            if(data.hasOwnProperty(key)) {
                self.remove(key);
            }
        }
    }


    /**
     * Removes a cache entry with the given key
     */
    this.remove = (key) => {
        delete data[key];
    }


}

module.exports = Cache;