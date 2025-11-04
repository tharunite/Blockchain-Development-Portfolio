import { expect } from "chai";
import { ethers } from "hardhat";

describe("Hello", function () {
  it("Should return and change message", async function () {
    const Hello = await ethers.getContractFactory("Hello");
    const hello = await Hello.deploy();
    await hello.waitForDeployment();

    expect(await hello.message()).to.equal("Hello Hardhat");

    await hello.setMessage("Hi Ethereum");
    expect(await hello.message()).to.equal("Hi Ethereum");
  });
});
