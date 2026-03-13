#1anshikaciphershukla
from Crypto.Cipher import PKCS1_OAEP 
from Crypto.PublicKey import RSA 
 
#Generate RSA key pair 
key=RSA.generate(2048) 
 
private_key=key 
public_key=key.publickey() 
 
#create cipher objects 
encrpytor=PKCS1_OAEP.new(public_key) 
decrpytor=PKCS1_OAEP.new(private_key) 
 
#message to encrypt 
message=b"hello RSA!" 
 
#encrypt 
encrpyted=encrpytor.encrypt(message) 
print("Encrypted:",encrpyted) 
 
#decrypt 
decrpyted=decrpytor.decrypt(encrpyted) 
print("Decrypted:",decrpyted.decode()) 
 


#anshikabinshuklaaschi
import binascii #used to convert data to hex string (human-readable) 
import Crypto  
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
 
class Client: 
    def __init__(self): 
        random=Crypto.Random.new().read 
        self._private_key=RSA.generate(1024,random) 
        self._public_key=self._private_key.publickey() 
        self._signer=PKCS1_v1_5.new(self._private_key) 
     
    @property 
    def identity(self): 
        return binascii.hexlify( 
            self._public_key.exportKey(format="DER") 
        ).decode("ascii") 
     
TYIT=Client() 
print("\n Public Key:", TYIT.identity) 



#6
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.13; 
 
contract tytoken{ 
    string public name = "tytoken"; 
    string public symbol = "TYT"; 
    uint256 public totalSupply; 
    mapping (address => uint256)public balanceOf; 
 
    constructor(uint256 initialSupply){ 
        totalSupply =initialSupply; 
        balanceOf[msg.sender]=initialSupply; 
    } 
 
    function transfer(address toWhom,uint256 value)public returns(bool 
success){ 
        require(balanceOf[msg.sender]>=value,"Insufficient"); 
        balanceOf[msg.sender]-=value; 
        balanceOf[toWhom]+=value; 
        return true; 
    } 
    
} 


#7ERC
 // SPDX-License-Identifier: MIT 
pragma solidity ^0.8.20; 
 
import "@openzeppelin/contracts/token/ERC20/ERC20.sol"; 
 
contract MyToken is ERC20{ 
    constructor() ERC20("MyToken", "MTK") { 
        _mint(msg.sender,1_000_000 ether); 
    } 
} 

#stake
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.20; 
 
import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; 
 
contract SimpleStaking { 
    IERC20 public token; 
    mapping (address=>uint256)public stakes; 
 
    constructor(address _token){ 
        token =IERC20(_token); 
    } 
    function stake(uint256 amount) external{ 
        require(amount >0 , "Zero amount"); 
        token.transferFrom(msg.sender,address(this),amount); 
        stakes[msg.sender] += amount; 
    } 
    function unstake(uint256 amount) external{ 
        require(stakes[msg.sender]>=amount,"Not enough Stake"); 
        stakes[msg.sender] -=amount; 
        token.transfer(msg.sender,amount); 
    } 
} 

#8attendance
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.9; 
 
contract Attendance { 
    // Stores roll number presence 
    mapping(uint256 => bool)public isPresent; 
 
    // Contructor initializes roll numbers 
    constructor(uint256[] memory rollno){ 
        for (uint256 i = 0; i < rollno.length;i++){ 
            isPresent[rollno[i]]=true; 
        } 
    } 
    // Check attendance 
    function attend(uint256 roll)public view returns(bool){ 
        return isPresent[roll]; 
    } 
} 

 

#8transferring from one to another account
// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.13; 
 
contract tytoken{ 
    string public name = "tytoken"; 
    string public symbol = "TYT"; 
    uint256 public totalSupply; 
    mapping (address => uint256)public balanceOf; 
 
    constructor(uint256 initialSupply){ 
        totalSupply =initialSupply; 
        balanceOf[msg.sender]=initialSupply; 
    } 
    
} 


