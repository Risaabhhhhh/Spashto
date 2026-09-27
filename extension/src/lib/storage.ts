export const storage = {
  get: (key: string): Promise<any> => {
    return new Promise((resolve) => {
      chrome.storage.local.get([key], (result) => {
        resolve(result[key]);
      });
    });
  },
  set: (key: string, value: any): Promise<void> => {
    return new Promise((resolve) => {
      chrome.storage.local.set({ [key]: value }, () => {
        resolve();
      });
    });
  },
  listen: (key: string, callback: (newValue: any) => void) => {
    chrome.storage.onChanged.addListener((changes, areaName) => {
      if (areaName === 'local' && changes[key]) {
        callback(changes[key].newValue);
      }
    });
  }
};
