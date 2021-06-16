export default function getFullResponseFromAPI(success) {
  return new Promise(function(resolve, reject){
    if (success == true) {
      resolve({ status: 200, body: 'Success' });
    } else if ( success == false ) {
      reject(Error('The fake API is not working currently'));
    }
  });
}
